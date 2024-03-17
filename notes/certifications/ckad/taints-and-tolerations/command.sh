kubectl taint nodes <node-name> key=value:taint-effect

taint-effects:
  - NoSchedule
  - PreferNoschedule
  - NoExecute
