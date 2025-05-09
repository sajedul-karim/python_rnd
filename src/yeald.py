def my_yeald():
    yield 'step 1'
    print('sk1')
    yield 'step 2'
    print('sk2')
    yield 'step 3'
    print('sk3')
result = my_yeald()
print('sk')
for step in result:
    print(f'step: {step}')
