beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beer_up = {be : beer[be]*1.05 for be in beer}
print(f'{beer}')
print(f'{beer_up}')
