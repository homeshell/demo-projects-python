//  Libraries 
import java.util.concurrent.TimeUnit;
import java.util.ArrayList;
import java.util.Scanner;
public class Java_Factorial_Calculator {
    public static void main(String[] args) throws InterruptedException {
        //  Starts user with fresh terminal to work with.
        clearScreen();
        //  Delcares Variables
        Scanner scan = new Scanner(System.in);
        int calcFactorial = 1;
        int num1 = 0;
        int numOfCalculations = 0;
        int iterateArray = 0;
        int add_upAll = 0;
        ArrayList<Integer> storedChoices = new ArrayList<Integer>();
        String end_or_continueLoop;
        String inputFactorial = "";
        boolean factorial_loop = true;
        boolean validate_input = true;
        //  Masterloop
        while(factorial_loop == true) {
            //  Gets user input with exception handling.
            while (validate_input == true) {
                System.out.print("\nEnter number to calculate the factorial of: ");
                inputFactorial = scan.next();
                try { 
                    num1 = Integer.parseInt(inputFactorial);
                    validate_input = false;
                }
                catch(NumberFormatException nfe) {
                    clearScreen();
                    System.out.println("\nError Message - Number is not an integer!");
                }
            }
            //  Resets validation loop & stores user's choice.
            clearScreen();
            validate_input = true;
            storedChoices.add(iterateArray, num1);
            iterateArray++;
            System.out.println();
            System.out.println("CALCULATING...");
            //  Factorial calculator
            for (int i = num1; i >= 1; i--) {
                TimeUnit.SECONDS.sleep(1);
                System.out.println(num1 + "!" + " = " + calcFactorial + "*" + i);
                calcFactorial = calcFactorial * i;          
            }
            //  Tallies up total number of times the user does a calculation & adds up the sum of all calculations.
            numOfCalculations++;
            add_upAll = add_upAll + calcFactorial;
            //  Prints the previously inputted number's factorial calculation.
            System.out.println("\n" + num1 + "! is equal to " + calcFactorial + ".");
            //  Prompts user to either continue or end the program.
            System.out.print("\nDo you wish to calculate another factorial? ");
            end_or_continueLoop = scan.next();
            //  Input validation
            while(end_or_continueLoop.equalsIgnoreCase("NO") != true && end_or_continueLoop.equalsIgnoreCase("YES") != true) {
                System.out.print("\nDo you wish to calculate another factorial? (Yes / No) ");
                end_or_continueLoop = scan.next();
            } 
            //  Displays total times program ran, sum of all factorials, which numbers they chose & terminates the program.
            if (end_or_continueLoop.equalsIgnoreCase("No")) {
                clearScreen();
                System.out.println("\n" + "Excellent! " + numOfCalculations + " factorials have been calculated in this program, with a sum total of: " + add_upAll);
                System.out.println("Here's all your number choices, given in order: " + storedChoices.toString());
                TimeUnit.SECONDS.sleep(3);
                factorial_loop = false;
            }
            //  Resets terminal and factorial variable.
            else {
                clearScreen();
                calcFactorial = 1;
            } 

        }
        //  Prevents memory leak
        scan.close();
    }      
        //  Method for clearing the terminal.
        public static void clearScreen() {  
            System.out.print("\033[H\033[2J");  
            System.out.flush();  
        }

}
    



