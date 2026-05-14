# customer-behavior-sim
A small Python simulation experiment for learning how customer behavior can change over time.

The goal is to build a tiny customer world where customers have simple traits and changing behavior.

- customers
- daily ticks
- usage score
- satisfaction score
- random variation
- an event log
- a simple report of what happened


## Planned loop 
```text
customers
→ simulation loop
→ events
→ reduced state
→ simple report
```

## Done when
- create a small set of customers
- simulate 90 days
- update usage and satisfaction
- log events for each day
- print a short summary of what happened

## To run 
```bash
pip install -e .
simulate
```

