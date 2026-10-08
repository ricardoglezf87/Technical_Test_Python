# room_capacity_test
**Context**

At Fuertafit, our goal is to move the world by helping people improve their health and transform their bodies through a simple, step-by-step approach.
Every day, tens of thousands of users train through the platform, but traffic is not evenly distributed throughout the day. Usage is heavily concentrated around 7:00 a.m. and, especially, between 6:00 p.m. and 9:00 p.m.
During these peak periods, the platform can receive hundreds of thousands of room bookings within a single hour.
From a system-design perspective, this raises two important questions:

 - How many users overlap during the highest-demand period?
 - How long does that peak load last?

The duration of a traffic peak is just as important as its size. A spike lasting only one minute may not require any action, while sustained high demand for ninety minutes could justify increasing room capacity.
Understanding both peak concurrency and peak duration is therefore essential to make capacity decisions and prevent users from being unable to book a training session.
This is especially important because one of Fuertafit's core principles is that taking care of yourself should fit into any lifestyle. If users finally find time to train but there is no available capacity, the platform is not fulfilling that goal.
