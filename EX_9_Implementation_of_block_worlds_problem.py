#Ex N0: 9 IMPLEMENTATION OF BLOCK WORLDS PROBLEM 

#STRIPS

def strips_blocks_world():

    print("BLOCKS WORLD USING STRIPS\n")

    print("Enter Block Names")

    A = input("Block 1 : ")
    B = input("Block 2 : ")
    C = input("Block 3 : ")

    print("\nInitial State")
    print("----------------")

    print("ONTABLE(", A, ")", sep="")
    print("ONTABLE(", B, ")", sep="")
    print("ONTABLE(", C, ")", sep="")
    print("CLEAR(", A, ")", sep="")
    print("CLEAR(", B, ")", sep="")
    print("CLEAR(", C, ")", sep="")
    print("ARMEMPTY")

    print("\nEnter Goal")

    top = input("Top Block : ")
    middle = input("Middle Block : ")
    bottom = input("Bottom Block : ")

    print("\nGoal State")
    print("----------------")

    print("ON(", top, ",", middle, ")", sep="")
    print("ON(", middle, ",", bottom, ")", sep="")

    print("\nSTRIPS PLAN")
    print("----------------")
  
    print("\nStep 1")
    print("Action : PICKUP(", middle, ")", sep="")

    print("Precondition : ARMEMPTY, CLEAR(",
          middle, "), ONTABLE(", middle, ")", sep="")

    print("Delete : ARMEMPTY, ONTABLE(", middle, ")", sep="")

    print("Add : HOLDING(", middle, ")", sep="")

    print("\nStep 2")
    print("Action : STACK(", middle, ",", bottom, ")", sep="")

    print("Precondition : HOLDING(", middle,
          "), CLEAR(", bottom, ")", sep="")

    print("Delete : HOLDING(", middle,
          "), CLEAR(", bottom, ")", sep="")

    print("Add : ARMEMPTY, ON(", middle,
          ",", bottom, ")", sep="")

    print("\nStep 3")
    print("Action : PICKUP(", top, ")", sep="")

    print("Precondition : ARMEMPTY, CLEAR(",
          top, "), ONTABLE(", top, ")", sep="")

    print("Delete : ARMEMPTY, ONTABLE(", top, ")", sep="")

    print("Add : HOLDING(", top, ")", sep="")

    print("\nStep 4")
    print("Action : STACK(", top, ",", middle, ")", sep="")

    print("Precondition : HOLDING(", top,
          "), CLEAR(", middle, ")", sep="")

    print("Delete : HOLDING(", top,
          "), CLEAR(", middle, ")", sep="")

    print("Add : ARMEMPTY, ON(", top,
          ",", middle, ")", sep="")

    print("ON(", top, ",", middle, ")", sep="")
    print("ON(", middle, ",", bottom, ")", sep="")

    print("\nGoal State Achieved!")


strips_blocks_world()

