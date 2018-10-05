from planet import Planet

from calc import planet_mass, planet_vol

naboo=Planet('naboo',10,122)
naboo_mass=planet_mass(naboo.gravity,naboo.radius)
naboo_vol=planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volume {naboo_vol} ')

aa=naboo.spin()
print(aa)
print(naboo.commons())