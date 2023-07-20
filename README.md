# PoolSystem

## Problem Statement

As of now I'm not able to keep track of all the changes done in my pool like: reading - Ph, Chroline, Bromine, Alkalinity and Salt, When the reading was performe. Also keep records of when a maintenance was performed.
## Description

The poolsystem will report the number of readings in chronologica order performed to a given pool. A pool can be maintaned by multiples operators and one operator can have multiple pools.

## Entities

Pool - id, Alias, Location, type.
PoolReading - id, Timestamp, ph reading, salt reading, bromine reading, Akalinity reading(optional), temperature(optional), comment (optional), operator.
operator - id, name, last name, username, password.
PoolMaintenance - id, operator, comment, timestamp.

one pool has multiple readings
one pool has multiple PoolMaintenance
one pool has multiple operators

one operator has multiple pools
one operator has multiple readings
one operator has multiple PoolMaintenance


## Methods 

Create Pool
Delete Pool
Archive Pool
Update Pool

Create operator
Delete operator
Archive operator
Update operator

Create PoolReading
Delete PoolReading
Archive PoolReading
Update PoolReading

Create PoolMaintenance
Delete PoolMaintenance
Archive PoolMaintenance
Update PoolMaintenance