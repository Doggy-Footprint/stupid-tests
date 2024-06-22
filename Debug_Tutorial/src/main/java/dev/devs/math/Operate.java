package dev.devs.math;

@FunctionalInterface
public interface Operate<T extends Number> {
    double exec(T op1, T op2);
}
