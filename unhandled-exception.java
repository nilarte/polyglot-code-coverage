public class UnhandledExceptionExample {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3};
        
        // This will throw ArrayIndexOutOfBoundsException
        System.out.println("Value: " + numbers[5]);

        System.out.println("This line will never be reached.");
    }
}
