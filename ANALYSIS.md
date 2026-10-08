# Introduction and Document Objective

Fuertafit aims to help people improve their health and fitness through a simple and progressive method. The platform manages tens of thousands of users and bookings every day, and these bookings are not evenly distributed throughout the day.

The highest level of activity mainly occurs early in the morning, around 07:00, and during the period between 18:00 and 21:00. During these peak periods, the system may need to manage hundreds of thousands of bookings within the same time slot.

The objective of this document is to describe the functional analysis of the process used to determine the **maximum booking occupancy or concurrency**, as well as to identify the **start time and end time of the maximum occupancy period**.

This information will help analyze room demand and support decisions about opening new rooms or increasing capacity, with the objective of minimizing the number of users who cannot find availability.

# Maximum Occupancy Calculation

Each booking has a **start time** and an **end time**.

From the received list of bookings, the system must calculate and return the following information:

- Maximum number of concurrent bookings.
- Start time of the maximum occupancy period.
- End time of the maximum occupancy period.

The system will receive a list of bookings as input and must analyze all booking intervals to determine when the highest number of simultaneous bookings occurs.

For example:

`[(9, 12), (10, 13), (11, 14)]`

In this case, the maximum concurrency occurs between 11:00 and 12:00, when the three bookings overlap.

The expected result would be:

`(3, 11, 12)`

# Input Validation

Before performing the calculation, it is necessary to define which validations the system must apply to the received bookings.

The following rules have initially been identified:

- The system may receive an empty list of bookings.
- If a booking is provided, both the start time and the end time must contain a valid value and cannot be null.
- Times must be integer values without decimals.
- Time values greater than `23` will not be allowed unless another valid range is explicitly defined.
- Negative values will not be allowed.
- The start time cannot be later than the end time unless bookings that cross midnight are explicitly allowed.
- The expected behavior must be defined when the start time and end time are equal, for example `(10, 10)`.

Additionally, the system must consider the possibility of having **multiple periods with the same maximum occupancy level**. In this case, the rule used to select the interval to return must be defined.

# Questions to Confirm

After the initial analysis, the following functional questions have been identified and require clarification.

## 1. Consecutive Periods with the Same Maximum Occupancy

Consider the following example:

`[(9, 10), (10, 11), (11, 12)]`

The maximum occupancy is `1` during the complete period between 09:00 and 12:00.

However, the result provided in the example is:

`(1, 9, 10)`

Should the function return only the **first interval where the maximum occupancy is reached**, or should consecutive intervals with the same occupancy level be grouped and returned as one complete period?

If consecutive intervals are grouped, the result in this case would be:

`(1, 9, 12)`

## 2. Multiple Maximum Occupancy Periods

There may be several separate periods during the day with the same maximum occupancy.

For example, the maximum occupancy could be `5` between 09:00 and 10:00 and again between 18:00 and 19:00.

Since the function only returns one interval, it is necessary to define which rule should be used:

- Return the first period where the maximum occupancy is reached.
- Return the last period.
- Return the longest period.
- Apply another functional rule.

## 3. Valid Time Range

It is necessary to confirm the valid range for start and end times.

In particular:

- Must time values be between `0` and `23`?
- Can `24` be used as an end time?
- Can bookings cross midnight?

For example:

`(23, 2)`

If this is allowed, the interval should be interpreted as a booking that starts at 23:00 and ends at 02:00 on the following day.

## 4. Input Data Validation

It is necessary to confirm whether the function can assume that all received bookings are valid or whether it must validate the input data.

Possible cases to consider include:

- Same start and end time: `(10, 10)`.
- Negative values: `(-1, 10)`.
- Time values outside the allowed range: `(10, 25)`.
- End time earlier than start time: `(15, 10)`.
- Null values.
- Decimal values.

It should also be confirmed whether the function can assume that start and end times will always be integer values, as currently defined in the function signature.

# Improvement Proposal

As a possible functional and visual improvement, a graphical representation of occupancy throughout the day could be added.

The system could generate a structure containing the occupancy value for each hourly time slot. For example:

`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 8, 10, 6, 5, 3, 2, 1, 0, 0, 0, 0, 0]`

Each position would represent the occupancy for a specific hour.

A **color scale or heatmap** could then be applied to this information to make it easier to identify the periods with the highest occupancy.

For example:

- **Green:** low or no occupancy.
- **Intermediate colors:** medium occupancy.
- **Red:** maximum occupancy or occupancy close to the capacity limit.

In the previous example, a value of `0` could be displayed in green, an intermediate value such as `5` could use a color between green and red, and the maximum value `10` could be displayed in red.

The limits used to determine the colors should be configurable through parameters or calculated dynamically based on factors such as:

- Number of available rooms.
- Maximum capacity of each room.
- Total available capacity.
- Alert thresholds defined by the business.

This representation would make it easier to quickly detect high-demand or saturated periods and would support decisions related to opening new rooms or increasing capacity.

# Use of Artificial Intelligence

Artificial Intelligence tools have been used as a support tool during the development and documentation process.
The use of AI has been focused on the following activities:

- Massive testing: GPT was used to execute the implemented code with large sets of input data in order to test its behavior, identify possible edge cases, and verify the solution under a high number of bookings.
- Translations: AI was used to translate documentation from Spanish to English.

The implementation and technical decisions were made and reviewed manually. 