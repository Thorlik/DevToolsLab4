# UnitTests

## Sum

| Test Name             | Input Data  | Expected output | Result  |
| --------------------- | ----------- | --------------- | ------- |
| test_zero_summ        | 0 + 19      | 19              | true    |
| test_negatives_summ   | -50 + -6    | -56             | true    |

## Subtraction

| Test Name         | Input Data        | Expected output | Result  |
| ----------------- | ----------------- | --------------- | ------- |
| test_poz_sub      | 2 - 25            | -23             | true    |
| test_floats_sub   | 100.345 - 499.2   | 501.15          | true    |

## Multiplication

| Test Name                | Input Data  | Expected output | Result  |
| ------------------------ | ----------- | --------------- | ------- |
| test_negatives_mul       | -5 * -60    | 300             | true    |
| test_zero_mul            | 0 * 60530   | 0               | true    |

## Division

| Test Name         | Input Data                  | Expected output       | Result  |
| ----------------- | --------------------------- | --------------------- | ------- |
| test_big_div      | 8979456112398 / 976541346   | 9195.16               | true    |
| test_zero_div     | 36 / 0                      | На ноль делить нельзя | true    |

## Wrong Operation

| Test Name             | Input Data  | Expected output       | Result  |
| --------------------- | ----------- | --------------------- | ------- |
| test_wrong_operation  | 5 d 5       | Неизвестная операция  | true    |