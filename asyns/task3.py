import asyncio


async def sowing(*plants):
    plant_sp = []
    for plant in plants:
        plant_sp.append(general(*plant))
    await asyncio.gather(*plant_sp)


async def general(*plant):
    print(f'0 Beginning of sowing the {plant[0]} plant')
    tasks = [main_process(*plant), additional_process_1(*plant),
             additional_process_2(*plant)]
    await asyncio.gather(*tasks)
    print(f'9 The seedlings of the {plant[0]} are ready')


async def main_process(plant, soa_time, germination_time, survival_time):
    print(f'1 Soaking of the {plant} started')
    await asyncio.sleep(soa_time / 1000)
    print(f'2 Soaking of the {plant} is finished')
    print(f'3 Shelter of the {plant} is supplied')
    await asyncio.sleep(germination_time / 1000)
    print(f'4 Shelter of the {plant} is removed')
    print(f'5 The {plant} has been transplanted')
    await asyncio.sleep(survival_time / 1000)
    print(f'6 The {plant} has taken root')


async def additional_process_1(plant, soa_time, germination_time, survival_time):
    print(f'8 Treatment of {plant} from pests')
    await asyncio.sleep(5 / 1000)
    print(f'8 The {plant} is treated from pests')


async def additional_process_2(plant, soa_time, germination_time, survival_time):
    print(f'7 Application of fertilizers for {plant}')
    await asyncio.sleep(3 / 1000)
    print(f'7 Fertilizers for the {plant} have been introduced')


data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
asyncio.run(sowing(*data))
