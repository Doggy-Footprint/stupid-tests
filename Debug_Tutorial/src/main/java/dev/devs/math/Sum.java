package dev.devs.math;

public class Sum<T extends Number> extends TwoOperandOperation<T> {
    @Override
    protected void operateInternal() {
        this.result = this.op1.doubleValue() + this.op2.doubleValue();
    }
}
