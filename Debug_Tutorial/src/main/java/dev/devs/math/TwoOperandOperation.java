package dev.devs.math;

public abstract class TwoOperandOperation<T extends Number> {
    protected T op1;
    protected T op2;
    protected boolean operandSet;
    protected boolean done;
    protected double result;


    TwoOperandOperation() {
        this.operandSet = false;
        this.done = false;
    }

    public void updateOperands(T op1, T op2) {
        this.op1 = op1;
        this.op2 = op2;
        this.operandSet = true;
    }

    public void operate() {
        if (this.operandSet) {
            operateInternal();
            this.done = true;
        }
    }

    protected abstract void operateInternal();

    public Double getResult() {
        if (this.done) {
            this.done = false;
            return this.result;
        }
        return null;
    }
}
