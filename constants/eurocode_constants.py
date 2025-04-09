DEFAULT_DELTA_C_DEV = 5
DELTA_C_DEV_DESCRIPTION = (
    "(deviation) according to art. 4.4.1.3 (1). "
    f"The recommended value according to the Netherlands National Annex, is {DEFAULT_DELTA_C_DEV}."
)

DEFAULT_DELTA_C_DUR_GAMMA = 0
DELTA_C_DUR_GAMMA_DESCRIPTION = (
    "An additional safety requirement based on art. 4.4.1.2 (6). "
    f"The recommended value according to the Netherlands National Annex is {DEFAULT_DELTA_C_DUR_GAMMA}."
)

DEFAULT_DELTA_C_DUR_ST = 0
DELTA_C_DUR_ST_DESCRIPTION = (
    "A reduction of minimum concrete cover when using stainless steel based on art. 4.4.1.2 (7). "
    f"The recommended value according to the Netherlands National Annex is {DEFAULT_DELTA_C_DUR_ST}."
)

DEFAULT_DELTA_C_DUR_ADD = 0
DELTA_C_DUR_ADD_DESCRIPTION = (
    "A reduction of minimum concrete cover when using additional protection based on art. 4.4.1.2 (8). "
    f"The recommended value according to the Netherlands National Annex is {DEFAULT_DELTA_C_DUR_ADD}."
)

DELTAS = {
    "dev": {"default": DEFAULT_DELTA_C_DEV, "description": DELTA_C_DEV_DESCRIPTION, "uname": "$Δc_{dev}$"},
    "dur_gamma": {
        "default": DEFAULT_DELTA_C_DUR_GAMMA,
        "description": DELTA_C_DUR_GAMMA_DESCRIPTION,
        "uname": "$Δc_{dur,γ}$",
    },
    "dur_st": {
        "default": DEFAULT_DELTA_C_DUR_ST,
        "description": DELTA_C_DUR_ST_DESCRIPTION,
        "uname": "$Δc_{dur,st}$",
    },
    "dur_add": {
        "default": DEFAULT_DELTA_C_DUR_ADD,
        "description": DELTA_C_DUR_ADD_DESCRIPTION,
        "uname": "$Δc_{dur,add}$",
    },
}

ABRASION_CLASS_DESCRIPTION = (
    "Abrasion class of the concrete surface according to art. 4.4.1.2 (13). "
    "The recommended values according to the Netherlands National Annex are:\\\n"
    "XM1: 0\\\n"
    "XM2: 0\\\n"
    "XM3: 0"
)
