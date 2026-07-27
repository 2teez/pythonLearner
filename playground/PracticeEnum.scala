package com.scalapractice.enums

enum Weekday:
    case Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

@main def main(args: String*): Unit =
    val weekday = Array(
        Weekday.Monday, Weekday.Tuesday, Weekday.Wednesday,
        Weekday.Thursday, Weekday.Friday, Weekday.Saturday, Weekday.Sunday
    )
    println(weekday.mkString(", "))
