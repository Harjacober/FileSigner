
#True==>Doesn't support multiline comments

#False==>Supports multiline comments

symbols = {"py": ('"""','"""',False),
            "java": ('/*','*/',False),
            "js": ('/*','*/',False),
            "c": ('/*','*/',False),
            "php": ('/*','*/',False),
            "kt": ('/*','*/',False),
            "go": ('/*','*/',False),
            "pl": ('/*','*/',False),
            "rb": ('=','=',False),
            "xml": ('<!--','-->',False),
            "cofee": ('###','###',False),
            "css": ('/*','*/',False),
            "html": ('<!--','-->',False),
            "dart": ('/*','*/',False),
            "R" :('#','#',True),
           "scala": ('"""', '"""',False),
           "swift": ('"""', '"""',False),
           "cs": ('@"', '"',False)
           }

