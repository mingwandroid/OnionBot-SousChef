{
    1: {
        "message": "Place a pan on the hob to start",
        1: {"func": _set_classifiers, "args": {"value": "pan_on_off,sauce,stirring"}},
        2: {"func": _set_hob_off},
        3: {"func": _classify, "args": {"model": "pan_on_off", "label": "pan_on"}},
    },
    2: {
        "message": "Add a tbsp of olive oil",
        1: {"func": _classify, "args": {"model": "sauce", "label": "add_oil"}},
    },
    3: {
        "message": "Heating until pan is hot",
        1: {"func": _start_pan_detector},
        2: {"func": _set_fixed_setpoint, "args": {"value": 40}},
        3: {"func": _poll_temperature, "args": {"target": 80}},
    },
    4: {
        "message": "Add 2 chopped onions",
        1: {"func": _classify, "args": {"model": "sauce", "label": "add_onions"}},
        2: {"func": _set_fixed_setpoint, "args": {"value": 10}},
    },
    5: {
        "message": "Cooking on a low heat until soft",
        1: {"func": _start_stir_detector, "args": {"duration": 60}},
        2: {"func": _classify, "args": {"model": "sauce", "label": "onions_cooked"}},
    },
    6: {
        "message": "Stir in 1 tbsp of tomato puree",
        1: {"func": _classify, "args": {"model": "sauce", "label": "add_puree"}},
    },
    7: {
        "message": "Cooking for 2 minutes",
        1: {"func": _start_timer, "args": {"name": "puree", "duration": 2*60}},
        2: {"func": _poll_timer, "args": {"name": "puree"}},
    },
    8: {
        "message": "Add 2x400g cans of chopped tomatoes",
        1: {"func": _classify, "args": {"model": "sauce", "label": "add_tomatoes"}},
    },
    9: {
        "message": "Simmering for 20 minutes",
        1: {"func": _set_fixed_setpoint, "args": {"value": 30}},
        2: {"func": _start_timer, "args": {"name": "simmer", "duration": 20*60}},
        3: {"func": _poll_timer, "args": {"name": "simmer"}},
    },
    10: {"message": "Tomato sauce is ready!", 
            1: {"func": _set_hob_off},
        },
}
