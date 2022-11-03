import java.util.HashMap;

public class CircleGame {
    public static void main(String[] args) {
        int numPlayers = 465;
        int numMarbles = 7194000;
        int curMarble = 0;
        HashMap<Integer, Long> scores = new HashMap<>();
        Node curNode = new Node(null, null, 0);
        Node startNode = curNode;
        int player = 0;
        curNode.setNext(curNode);
        curNode.setPrev(curNode);

        while(curMarble < numMarbles) {
            int newMarble = curMarble + 1;
            player = (player + 1) % numPlayers;
            if (newMarble % 23 == 0) {
                for (int i = 0; i < 7; i++) {
//                    System.out.println(curNode.getValue());
                    curNode = curNode.getPrev();
                }

                long curScore = curNode.getValue() + newMarble;
                if (!scores.containsKey(player)) {
                    scores.put(player, curScore);
                } else {
                    scores.put(player, scores.get(player) + curScore);
                }

                curNode = curNode.remove();
            } else {
                curNode = curNode.getNext().insertNode(newMarble);
            }
            curMarble = newMarble;
//            printNodes(player, startNode, curNode);
        }
        System.out.println(scores);
        System.out.println(scores.values().stream().mapToLong(v -> v).max().orElse(0));
    }

    public static void printNodes(int player, Node startNode, Node currentNode) {
        Node curNode = startNode.getNext();
        StringBuilder result = new StringBuilder();
        result.append(startNode.getValue());

        while(startNode != curNode) {
            result.append(" ");
            if (curNode == currentNode) {
                result.append("(");
                result.append(curNode.getValue());
                result.append(")");
            } else {
                result.append("" + curNode.getValue());
            }
            curNode = curNode.getNext();
        }
        System.out.println("[" + player + "] " + result.toString());
    }
}
