import instructions

instruction_set = {
    "ADD": instructions.add,
    "SUB": instructions.sub,
    "TIMES": instructions.times,
    "DIV": instructions.div,
    "MOD": instructions.mod,
    "CMP": instructions.cmp,
    "GREATER": instructions.greater,
    "LESS": instructions.less,
    "EQUAL": instructions.equal,
    "ISNIL": instructions.isnil,
    "ISPOS": instructions.ispos,
    "ISNEG": instructions.isneg,
    "JUMP": instructions.jump,
    "JUMPC": instructions.jumpc,
    "JSR": instructions.jsr,
    "SKIP": instructions.skip,
    "LINK": instructions.link,
    "STOP": instructions.stop,
    "PUSHABS": instructions.pushabs,
    "STOREABS": instructions.storeabs,
    "PUSHOFF": instructions.pushoff,
    "STOREOFF": instructions.storeoff,
    "POPFB": instructions.popfbr,
    "PUSHIMM": instructions.pushimm,
    "ADDSP": instructions.addsp
}