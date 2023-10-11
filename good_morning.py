import time

timestamp = time.strftime('%H:%M:%S')
print("Current time:", timestamp)

# Extract hour, minute, and second separately
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

# Check the time and print the appropriate message
if hour < 12:
    print("GOOD MORNING SIR")
elif hour == 12:
    print("IT'S NOON SIR")
elif hour < 12:
    print("GOOD AFTERNOON")
elif hour <17:
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")
