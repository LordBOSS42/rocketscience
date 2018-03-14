from ggrocket import Rocket, Planet

earth = Planet (viewscale=0.00005)
rocket = Rocket (earth, altitude=4000000, velocity=7904.50720939, timezoom=1)
earth.run (rocket)
