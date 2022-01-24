package 자료구조.java;
import java.util.PriorityQueue;
import java.util.Collections;

public class DoublepriorityQ {

    public int[] solution(String[] operations) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        PriorityQueue<Integer> priorityQueueMax = new PriorityQueue<>(Collections.reverseOrder());

        int[] answer = {0, 0};
        for (String o : operations) {
            String[] splitResult = o.split(" ");
            String oper = splitResult[0];
            int n = Integer.parseInt(splitResult[1]);
            if (oper.equals("I")) {
                priorityQueue.add(n);
                priorityQueueMax.add(n);
            } else if (!priorityQueue.isEmpty() && !priorityQueueMax.isEmpty()) {
                if (n < 0) {
                    int minValue = priorityQueue.poll();
                    priorityQueueMax.remove(minValue);
                } else {
                    int maxValue = priorityQueueMax.poll();
                    priorityQueue.remove(maxValue);
                }
            }
        }
        if (!priorityQueue.isEmpty()) {
            return new int[]{priorityQueueMax.peek(), priorityQueue.peek()};
        } else {
            return new int[]{0, 0};
        }
    }
}
