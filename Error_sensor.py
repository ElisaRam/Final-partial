https://replit.com/join/ozammfjgkq-elisaramirez4

def calculate_error_rate(temperatures):
  total_readings = 0
  error_count = 0

  for temp in temperatures:
      total_readings += 1
      if temp < 10 or temp > 40:
          error_count += 1

  error_rate = (error_count / total_readings) * 100 if total_readings > 0 else 0
  return error_count, error_rate

def get_temperature_readings():
  print("How many temperature readings do you have?")
  num_readings = int(input())

  temperature_readings = []

  for i in range(num_readings):
      temperature = float(input("Insert temperature {}: ".format(i + 1)))
      temperature_readings.append(temperature)

  return temperature_readings

def display_results(error_count, error_rate):
  print("The sensor went wrong", error_count, "times.")
  print("The sensor error rate is", error_rate, "%.")

temperature_readings = get_temperature_readings()
error_count, error_rate = calculate_error_rate(temperature_readings)
display_results(error_count, error_rate)
