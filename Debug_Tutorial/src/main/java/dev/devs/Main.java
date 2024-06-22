package dev.devs;

import dev.devs.math.*;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Sum<Double> sumDub_A = new Sum<>();
        Sum<Double> sumDub_B = new Sum<>();
        Sum<Float> sumFloat = new Sum<>();

        Double result1;
        Double result2;
        Double result3;

        System.out.println("Start Operations");

        sumDub_A.updateOperands(34.0, 654.0);
        sumDub_B.updateOperands(12.0, 53.0);
        sumFloat.updateOperands(25.2f, 53.3f);


        sumDub_A.operate();
        result1 = sumDub_A.getResult();
        sumDub_B.operate();
        result2 = sumDub_B.getResult();
        sumFloat.operate();
        result3 = sumFloat.getResult();

        StringBuilder sb
                = new StringBuilder()
                            .append("Results are: ")
                            .append(result1)
                            .append(", ")
                            .append(result2)
                            .append(", ")
                            .append(result3);
        System.out.println(sb);

        Main.runCustomSum(10, 11, 353, 345);

        MessageDigester md = null;
        try {
            md = new MessageDigester("MD5");
            md.update("Hello World");
            String digest = md.digest();
            System.out.println(digest);
        } catch (NoSuchAlgorithmException e) {
            System.out.println("failed to find message digest algorithm instance");
        }
    }

    public static void runCustomSum(Integer op1, Integer op2, Integer op3, Integer op4) {
        CustomSum<Integer> customSum = new CustomSum<>((operand1, operand2) -> operand1 + operand2 + 100);

        Double customResult;

        customSum.updateOperands(op1, op2);

        customSum.operate();
        customResult = customSum.getResult();

        System.out.println("Result is: " + customResult);

        customSum.updateOperands(op3, op4);

        customSum.updateOperate(((operand1, operand2) -> (double)(operand1 + operand2)/2.0 ));

        customSum.operate();
        customResult = customSum.getResult();

        System.out.println("Result is: " + customResult);
    }


}