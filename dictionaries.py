import instructions

instruction_set = {
    "ADD": instructions.add,
    "ADDF": instructions.addf,
    "SUB": instructions.sub,
    "SUBF": instructions.subf,
    "TIMES": instructions.times,
    "TIMESF": instructions.timesf,
    "DIV": instructions.div,
    "DIVF": instructions.divf,
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
    "LINK": instructions.link,
    "STOP": instructions.stop,
    "PUSHABS": instructions.pushabs,
    "STOREABS": instructions.storeabs,
    "PUSHOFF": instructions.pushoff,
    "STOREOFF": instructions.storeoff,
    "POPFBR": instructions.popfbr,
    "PUSHIMM": instructions.pushimm,
    "PUSHIMMF": instructions.pushimmf,
    "ADDSP": instructions.addsp,
    "PUSHSP": instructions.pushsp,
    "POPSP": instructions.popsp,
    "UNLINK": instructions.unlink,
    "JUMPIND": instructions.jumpind
}