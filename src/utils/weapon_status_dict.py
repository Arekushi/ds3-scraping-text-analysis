weapon_status_dict = {
    'type': [
        ['weapon_type', 'weapon-type', 'div', 'str'],
        ['attack_type', 'atk-type', 'div', 'str']
    ],
    'price': [
        ['buy_price', 'buy-price', 'td', 'int'],
        ['price', 'price', 'td', 'int']
    ],
    'skill': [
        ['skill_name', 'spc-atk', 'td', 'str'],
        ['fp_cost', 'focus-req', 'td', 'str'],
        ['fp_farron_cost', 'ring-cost', 'td', 'str'],
    ],
    'attack_power': [
        ['physical_attack', 'phys-atk', 'td', 'int'],
        ['magic_attack', 'mag-atk', 'td', 'int'],
        ['fire_attack', 'fire-atk', 'td', 'int'],
        ['lightning_attack', 'ltn-atk', 'td', 'int'],
        ['dark_attack', 'dark-atk', 'td', 'int'],
        ['critical_attack', 'counter', 'td', 'int'],
    ],
    'guard_absorption': [
        ['physical_defense', 'phys-def', 'td', 'float'],
        ['magic_defense', 'mag-def', 'td', 'float'],
        ['fire_defense', 'fire-def', 'td', 'float'],
        ['lightning_defense', 'ltn-def', 'td', 'float'],
        ['dark_defense', 'dark-def', 'td', 'float'],
        ['stability', 'stability', 'td', 'int'],
    ],
    'additional_effects': [
        ['bleed', 'bld-atk', 'td', 'int'],
        ['poison', 'psn-atk', 'td', 'int'],
        ['frost', 'fst-atk', 'td', 'int'],
    ],
    'miscellaneous': [
        ['range', 'shot-range', 'td', 'int'],
        ['spell_buff', 'cast-bonus', 'td', 'int'],
        ['durability', 'durability', 'td', 'int'],
        ['weight', 'weight', 'td', 'float'],
    ],
    'attribute_bonus': [
        ['strenght', 'str-bonus', 'td', 'str'],
        ['dexterity', 'dex-bonus', 'td', 'str'],
        ['intelligence', 'int-bonus', 'td', 'str'],
        ['faith', 'fth-bonus', 'td', 'str'],
    ],
    'attribute_requirement': [
        ['strenght', 'str-req', 'td', 'int'],
        ['dexterity', 'dex-req', 'td', 'int'],
        ['intelligence', 'int-req', 'td', 'int'],
        ['faith', 'fth-req', 'td', 'int'],
    ]
}
