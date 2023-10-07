from castle_map import read_input, CastleGraph, write_output


def main(input_file, output_file):
    N, M, castle_map = read_input(input_file)

    castle_graph = CastleGraph(N, M, castle_map)
    castle_graph.build_graph()
    max_rooms, max_coins = castle_graph.find_maximum_rooms_and_coins()

    write_output(output_file, max_rooms, max_coins)


if __name__ == "__main__":
    input_file = "input/input1.txt"  # Update with your input file path
    output_file = "output/output1.txt"  # Update with your output file path
    main(input_file, output_file)
