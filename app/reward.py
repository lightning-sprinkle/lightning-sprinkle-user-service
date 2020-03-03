import threading
import config

bucket = config.max_hourly_reward

def fill_bucket():
  """
  Make sure the bucket stays filled by adding the 1/60 of the max_hourly_reward
  every minute.
  """
  global bucket
  threading.Timer(60, fill_bucket).start()
  bucket = min(bucket + (config.max_hourly_reward / 60), config.max_hourly_reward)

def get_current_reward():
  """
  Calculate the current reward based on the level of the bucket
  """
  global bucket
  reward = int(bucket * 0.25)
  bucket = bucket - reward
  return reward
