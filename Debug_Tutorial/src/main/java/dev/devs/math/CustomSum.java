package dev.devs.math;

public class CustomSum<T extends Number> extends TwoOperandOperation<T> {
    private Operate<T> operate;

    public CustomSum(Operate<T> operate) {
        super();
        this.operate = operate;
    }

    @Override
    protected void operateInternal() {
        this.result = operate.exec(this.op1, this.op2);
    }

    public void updateOperate(Operate<T> operate) {
        this.operate = operate;
    }
}