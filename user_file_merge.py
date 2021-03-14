#This would be temp saved, written by the user and will be tested against the original file. !! Yes, I know this is the same as original_merge. This is temporary in the GitHub and will be removed later.
# --------------------------------------------------------------------------- Final array combination assignment
final = []
# --------------------------------------------------------------------------- Start generation of final 
def generate(arr):
    try:
        if len(arr) > 1:
    # --------------------------------------------------------------------------- 
            mid = len(arr)//2
    # --------------------------------------------------------------------------- 
            Left = arr[:mid]
    # --------------------------------------------------------------------------- 
            Right = arr[mid:]
    # --------------------------------------------------------------------------- 
            generate(Left)
    # ---------------------------------------------------------------------------
            generate(Right)
    # ---------------------------------------------------------------------------
            o = z = k = 0
    # ---------------------------------------------------------------------------
            while o < len(Left) and z < len(Right):
                if Left[o] < Right[z]:
                    arr[k] = Left[o]
                    o += 1
                else:
                    arr[k] = Right[z]
                    z += 1
                k += 1
    # ---------------------------------------------------------------------------
            while o < len(Left):
                arr[k] = Left[o]
                o += 1
                k += 1
    # ---------------------------------------------------------------------------
            while z < len(Right):
                arr[k] = Right[z]
                z += 1
                k += 1
    finally:
        final.clear()
    # ---------------------------------------------------------------------------
def compile(arr):
    for o in range(len(arr)):
        final.append(arr[o])
# ---------------------------------------------------------------------------
def solution(arr):
    generate(arr)
    compile(arr)
    return final
    #return finals
    #^^ Remove the '#' to purposely throw an error, and see the modified Case output.
# ---------------------------------------------------------------------------
