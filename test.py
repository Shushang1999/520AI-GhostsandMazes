
with open("output.txt","a") as o:
    o.write(str(datetime.datetime.now()))
# while True:
for i in range(0,201,5):
    for _ in range(0,100):
        output.append(run_agent1(no_of_ghosts))
    with open("output.txt","a") as o:
        o.write("Agent 1\n")
        o.write("No of Ghosts = {}\n" .format(no_of_ghosts))
        o.write("No of Mazes = 100\n")
        o.write("Successfull tries = {}\n" .format(globalVariables.success_count))
        o.write("{}\n".format(output))
    no_of_ghosts = no_of_ghosts + 1
    output.clear()
    globalVariables.success_count = 0
with open("output.txt","a") as o:
    o.write(str(datetime.datetime.now()))