package dev.devs.math;

public class OperandException extends Exception{
    public OperandException() {
        super("Operands are not set.");
    }

    public OperandException(String message) {
        super(message);
    }

}
