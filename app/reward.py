import threading

bucket = 0
max_hourly_reward = 40

def feed_bucket():
  """
  Make sure the bucket stays filled by adding the 1/60 of the max_hourly_reward
  every minute.
  """
  global bucket
  global max_hourly_reward

  threading.Timer(1, feed_bucket).start()
  bucket = min(bucket + (max_hourly_reward / 60), max_hourly_reward)
  print("bucket filled")
  print(bucket)
