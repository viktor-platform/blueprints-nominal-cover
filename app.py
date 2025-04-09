from blueprints.checks.nominal_concrete_cover.constants.constants_nen_en_1992_1_1_a1_2020 import (
    NominalConcreteCoverConstants2020A1,
)
from blueprints.checks.nominal_concrete_cover.definitions import AbrasionClass
from blueprints.checks.nominal_concrete_cover.definitions import CastingSurface
from blueprints.checks.nominal_concrete_cover.nominal_concrete_cover import NominalConcreteCover
from blueprints.codes.eurocode.nen_en_1992_1_1_a1_2020.chapter_4_durability_and_cover.table_4_1 import Carbonation
from blueprints.codes.eurocode.nen_en_1992_1_1_a1_2020.chapter_4_durability_and_cover.table_4_1 import Chemical
from blueprints.codes.eurocode.nen_en_1992_1_1_a1_2020.chapter_4_durability_and_cover.table_4_1 import Chloride
from blueprints.codes.eurocode.nen_en_1992_1_1_a1_2020.chapter_4_durability_and_cover.table_4_1 import ChlorideSeawater
from blueprints.codes.eurocode.nen_en_1992_1_1_a1_2020.chapter_4_durability_and_cover.table_4_1 import FreezeThaw
from blueprints.codes.eurocode.nen_en_1992_1_1_a1_2020.chapter_4_durability_and_cover.table_4_1 import (
    Table4Dot1ExposureClasses,
)
from blueprints.codes.eurocode.nen_en_1992_1_1_a1_2020.chapter_4_durability_and_cover.table_4_3 import (
    Table4Dot3ConcreteStructuralClass,
)
from blueprints.materials.concrete import ConcreteMaterial
from blueprints.materials.concrete import ConcreteStrengthClass
from constants.eurocode_constants import DEFAULT_DELTA_C_DUR_ADD
from constants.eurocode_constants import DEFAULT_DELTA_C_DUR_GAMMA
from constants.eurocode_constants import DEFAULT_DELTA_C_DUR_ST
from helper_functions.katex_html_template import katex_template
from munch import Munch
from parametrization import ConcreteCoverParametrization

from viktor.core import ViktorController
from viktor.views import WebResult
from viktor.views import WebView


class ConcreteCoverController(ViktorController):
    """controller class for concrete cover."""

    viktor_enforce_field_constraints = True

    label = "Concrete cover"
    parametrization = ConcreteCoverParametrization()

    def exposure_classes(self, params: Munch, **kwargs) -> Table4Dot1ExposureClasses:
        """Get the exposure classes."""
        return Table4Dot1ExposureClasses(
            carbonation=Carbonation(params.carbonation),
            chloride=Chloride(params.chloride),
            chloride_seawater=ChlorideSeawater(params.chloride_seawater),
            freeze=FreezeThaw(params.freeze_thaw),
            chemical=Chemical(params.chemical),
        )

    def structural_class(self, params: Munch, **kwargs) -> Table4Dot3ConcreteStructuralClass:
        """Get the structural class."""
        return Table4Dot3ConcreteStructuralClass(
            exposure_classes=self.exposure_classes(params),
            design_working_life=params.design_working_life,
            concrete_material=ConcreteMaterial(ConcreteStrengthClass(params.concrete_strength_class)),
            plate_geometry=params.plate_geometry,
            quality_control=params.quality_control,
        )

    def nominal_cover(self, params: Munch, **kwargs) -> NominalConcreteCover:
        """Calculate the nominal concrete cover."""
        nominal_concrete_cover = NominalConcreteCover(
            reinforcement_diameter=params.reinforcement_diameter,
            nominal_max_aggregate_size=params.nominal_max_aggregate_size,
            constants=NominalConcreteCoverConstants2020A1(
                DEFAULT_DELTA_C_DEV=params.delta_c_dev if params.override_delta_c_dev else None
            ),
            structural_class=self.structural_class(params),
            carbonation=Carbonation(params.carbonation),
            chloride=Chloride(params.chloride),
            chloride_seawater=ChlorideSeawater(params.chloride_seawater),
            delta_c_dur_gamma=(
                params.delta_c_dur_gamma if params.override_delta_c_dur_gamma else DEFAULT_DELTA_C_DUR_GAMMA
            ),
            delta_c_dur_add=(params.delta_c_dur_add if params.override_delta_c_dur_add else DEFAULT_DELTA_C_DUR_ADD),
            delta_c_dur_st=(params.delta_c_dur_st if params.override_delta_c_dur_st else DEFAULT_DELTA_C_DUR_ST),
            casting_surface=CastingSurface(params.casting_surface),
            uneven_surface=params.uneven_surface,
            abrasion_class=AbrasionClass(params.abrasion_class),
        )

        return nominal_concrete_cover

    @WebView("Concrete cover calculation", duration_guess=1)
    def calculate(self, params: Munch, **kwargs) -> WebResult:
        """Calculate and show the nominal concrete cover."""
        structural_class = self.structural_class(params)
        nominal_concrete_cover = self.nominal_cover(params)

        return WebResult(
            html=katex_template.format(
                nominal_cover_calculation=nominal_concrete_cover.latex(),
                structural_class=structural_class.explanation,
            ),
        )
