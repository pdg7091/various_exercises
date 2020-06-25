# if you run 10 kilometres in 42 minutes and 42 seconds,
# what is your average pace (time per mile in minutes and seconds)
# and what is your average speed in miles per hour

sec_to_hr = 1/3600
min_to_hr = 1/60
km_to_miles = 0.62

time_hrs = (42*min_to_hr) + (42*sec_to_hr)
dist_to_miles = 10 * km_to_miles

av_speed = dist_to_miles/time_hrs

pace_dist = 1

pace_time_hr = round(pace_dist/av_speed, 2)
pace_time_min = round(pace_time_hr * 60, 2)
pace_time_sec = round(pace_time_min % 1, 2) * 60

print(
    f'Average pace per mile = {int(pace_time_min)} minutes and {int(pace_time_sec)} seconds.')
print(f'Average speed {av_speed:.2f} miles per hour.')
