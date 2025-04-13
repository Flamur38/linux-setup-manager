
#!/usr/bin/env bash

# Kill already running instances
killall -q polybar

# Wait until all bars are dead
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar only on the primary monitor
if type "xrandr" > /dev/null; then
    PRIMARY_MONITOR=$(xrandr --query | grep " primary" | cut -d" " -f1)
    MONITOR=$PRIMARY_MONITOR polybar --reload toph &
else
    polybar --reload toph &
fi

