from blueprints.checks.nominal_concrete_cover.definitions import AbrasionClass
from blueprints.checks.nominal_concrete_cover.definitions import CastingSurface
from blueprints.codes.eurocode.exposure_classes import Exposure
from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_4_durability_and_cover.table_4_1 import Carbonation
from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_4_durability_and_cover.table_4_1 import Chemical
from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_4_durability_and_cover.table_4_1 import Chloride
from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_4_durability_and_cover.table_4_1 import ChlorideSeawater
from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_4_durability_and_cover.table_4_1 import FreezeThaw
from blueprints.materials.concrete import ConcreteStrengthClass
from constants.eurocode_constants import ABRASION_CLASS_DESCRIPTION
from constants.eurocode_constants import DELTAS
from helper_functions.parametrization_helper import get_environment_description
from helper_functions.welcome_text import BLUEPRINTS
from helper_functions.welcome_text import EUROCODES
from helper_functions.welcome_text import LIMITATIONS
from helper_functions.welcome_text import OVERVIEW

from viktor.parametrization import BooleanField
from viktor.parametrization import FunctionLookup
from viktor.parametrization import Image
from viktor.parametrization import IsNotEqual
from viktor.parametrization import LineBreak
from viktor.parametrization import Lookup
from viktor.parametrization import Not
from viktor.parametrization import NumberField
from viktor.parametrization import OptionField
from viktor.parametrization import OutputField
from viktor.parametrization import Parametrization
from viktor.parametrization import Tab
from viktor.parametrization import Text

CONCRETE_STRENGTH_CLASSES = list(strength_class.value for strength_class in ConcreteStrengthClass)
EXPOSURE_CLASSES: list[Exposure] = [Carbonation, Chloride, ChlorideSeawater, FreezeThaw, Chemical]
CASTING_SURFACES = [casting_surface.value for casting_surface in CastingSurface]
ABRASION_CLASSES = [abrasion_class.value for abrasion_class in AbrasionClass]

DEFAULT_EXPOSURE_CLASSES = {
    "carbonation": "Not applicable",
    "chloride": "Not applicable",
    "chloride_seawater": "Not applicable",
    "freeze_thaw": "Not applicable",
    "chemical": "Not applicable",
}


class ConcreteCoverParametrization(Parametrization):
    """parametrization for concrete cover."""

    welcome = Tab("Welcome")
    welcome.overview = Text(OVERVIEW)
    welcome.eurocodes = Text(EUROCODES)
    welcome.limitations = Text(LIMITATIONS)
    welcome.empty_space = Text("")
    welcome.logo = Image("BP.png", max_width=180, align="left")
    welcome.blueprints = Text(BLUEPRINTS)
    design_parameters = Tab("Design parameters")
    design_parameters.design_working_life = OptionField(
        "Design working life",
        options=[50, 75, 100],
        suffix="years",
        default=100,
        name="design_working_life",
    )
    design_parameters.concrete_strength_class = OptionField(
        "Concrete strength class",
        CONCRETE_STRENGTH_CLASSES,
        default=CONCRETE_STRENGTH_CLASSES[0],
        name="concrete_strength_class",
    )
    design_parameters.line_break = LineBreak()
    design_parameters.diameter = NumberField(
        "Reinforcement diameter",
        suffix="mm",
        default=12,
        min=6,
        name="reinforcement_diameter",
    )
    design_parameters.aggregate_size = NumberField(
        "Nominal maximum aggregate size",
        suffix="mm",
        default=20,
        min=4,
        description="This is relevant for the calculation of the minimum cover with regard to bond (Table 4.2)\\\n"
        "If maximum aggregate size is greater than 32 mm, minimum cover with regard to bond will increase by 5 mm.",
        name="nominal_max_aggregate_size",
    )

    exposure_classes = Tab("Exposure classes")
    for _exposure in EXPOSURE_CLASSES:
        setattr(
            exposure_classes,
            _exposure.snake_case(),
            OptionField(
                _exposure.exposure_class_description(),
                _exposure.options(),
                default=DEFAULT_EXPOSURE_CLASSES[_exposure.snake_case()],
                flex=50,
                name=_exposure.snake_case(),
            ),
        )
        setattr(
            exposure_classes,
            f"{_exposure.snake_case()}_description",
            OutputField(
                "",
                value=FunctionLookup(get_environment_description, _exposure, Lookup(_exposure.snake_case())),
                flex=50,
                visible=IsNotEqual(Lookup(_exposure.snake_case()), "Not applicable"),
            ),
        )
        setattr(exposure_classes, f"line_break_{_exposure.snake_case()}", LineBreak())

    execution = Tab("Execution")
    execution.plate_geometry = BooleanField(
        "Member with slab geometry",
        default=False,
        flex=50,
        name="plate_geometry",
    )
    execution.quality_control = BooleanField(
        "Special quality control of the concrete production ensured",
        default=False,
        flex=50,
        name="quality_control",
    )
    execution.line_1 = Text("---")
    execution.casting_surface = OptionField(
        "Casting surface",
        CASTING_SURFACES,
        description="The casting surface of the concrete according to art. 4.4.1.3 (4)",
        default=CASTING_SURFACES[0],
        flex=50,
        name="casting_surface",
    )
    execution.uneven_surface = BooleanField(
        "Uneven surface",
        description="Is the surface uneven according to art. 4.4.1.2 (11)?\\\nIf yes, the nominal cover will increase by 5 mm.",
        default=False,
        flex=50,
        name="uneven_surface",
    )
    execution.line_2 = Text("---")
    for _delta, _properties in DELTAS.items():
        setattr(
            execution,
            f"{_delta}_default",
            OutputField(
                _properties["uname"],
                description=_properties["description"],
                suffix="mm",
                value=_properties["default"],
                flex=50,
                visible=Not(Lookup(f"override_delta_c_{_delta}")),
            ),
        )
        setattr(
            execution,
            _delta,
            NumberField(
                _properties["uname"],
                description=_properties["description"],
                suffix="mm",
                default=_properties["default"],
                min=0,
                flex=50,
                name=f"delta_c_{_delta}",
                visible=Lookup(f"override_delta_c_{_delta}"),
            ),
        )
        setattr(
            execution,
            f"override_delta_c_{_delta}",
            BooleanField(
                f"Override the Eurocode recommendation for {_properties['uname']}",
                default=False,
                flex=50,
                name=f"override_delta_c_{_delta}",
            ),
        )

    execution.line_3 = Text("---")
    execution.abrasion_class = OptionField(
        "Abrasion class",
        ABRASION_CLASSES,
        description=ABRASION_CLASS_DESCRIPTION,
        default=ABRASION_CLASSES[0],
        name="abrasion_class",
    )
