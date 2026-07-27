package com.practice.enums;

enum Weekday {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY;

    public String toString() {
        return name().toLowerCase();
    }
}

class PracticeEnum {

    public static void main(String[] args) {
        Weekday[] days = Weekday.values();
        for (Weekday day : days) {
            System.out.println(day);
        }
    }
}
