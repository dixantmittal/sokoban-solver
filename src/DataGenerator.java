import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Scanner;

public class DataGenerator {
    public static void main(String[] args) throws IOException {
        if (args.length < 2) {
            System.out.println("Error! Correct Syntax: java DataGenerator <input.txt> <output.txt>");
            System.exit(0);
        }
        Scanner reader = new Scanner(new File(args[0]));

        PrintWriter expert = new PrintWriter(new BufferedWriter(new FileWriter(args[1])));

        while (reader.hasNextLine()) {
            int idx = Integer.parseInt(reader.nextLine().replace("; ", ""));

            HashSet<Coordinate> goals = new HashSet<Coordinate>();
            HashSet<Coordinate> walls = new HashSet<Coordinate>();
            HashSet<Coordinate> boxes = new HashSet<Coordinate>();
            Coordinate player = new Coordinate(0, 0);

            for (int i = 0; i < 10; i++) {
                String row = reader.nextLine();
                for (int j = 0; j < 10; j++) {
                    switch (row.charAt(j)) {
                        case '@':
                            player = new Coordinate(i, j);
                            break;
                        case '.':
                            goals.add(new Coordinate(i, j));
                            break;
                        case '$':
                            boxes.add(new Coordinate(i, j));
                            break;
                        case '#':
                            walls.add(new Coordinate(i, j));
                            break;
                    }

                }
            }
            Problem problem = new Problem(walls, new State(boxes, player), goals);

            Search search = new Search(new Heuristics(goals, 'm'));

            String result = "" + idx + " : " + search.prioritySearch(problem, 'a');
            System.out.println(result);
            expert.println(result);

            if (reader.hasNextLine())
                reader.nextLine(); // remove blank line

        }
        expert.close();
    }
}
