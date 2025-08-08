## Corridas
### `001_950_WorkFlow_01_senior`: Corrida base del workflow senior con variables default:
  * Semilla `163393`
  * Num_iterations: 20
  * Num_leaves: 16
  * Min_data_in_leaf: 1000
  * Feature_fraction_bynode: 0.2
  * Feature Engineering Random Forest activado.
* Ganancias obtenidas:
  * 62.017
  * 61.827
  * 61.557
  * 61.677
  * 61.797
* Variables más importantes previo a la FEhist Reduccion dimensionalidad con canaritos
  1. rf_006_005 (1)
  2. ctrx_quarter_normalizado
  3. rf_010_007 (2)
  4. mprestamos_personales
  5. rf_009_005 (3)
  6. mpasivos_margen
  7. mcuentas_saldo
  8. rf_008_006 (4)
  9. rf_013_003 (5)
  10. cpayroll_trx
  11. mcaja_ahorro
  12. rf_019_004 (6)
  13. mpayroll_sobre_edad
  14. mtarjeta_visa_consumo
  15. rf_016_005 (7)
  16. vm_status01
  17. rf_011_013 (8)
  18. rf_014_013 (9)
  19. cproductos_delta2
  20. rf_001_001 (10)
  ... 1022 variables en total
* Variables más importantes post FEhist Reduccion dimensionalidad con canaritos
  1. rf_010_007 (1)
  2. mcaja_ahorro
  3. ctrx_quarter_normalizado
  4. ctrx_quarter
  5. ctrx_quarter_normalizado_lag1
  6. cdescubierto_preacordado_delta2
  7. vm_status01
  8. rf_006_005 (2)
  9. rf_012_007 (3)
  10. ctarjeta_visa_transacciones
  11. cproductos_delta2
  12. ctrx_quarter_lag1
  13. mtarjeta_visa_consumo
  14. rf_016_005 (4)
  15. mcuentas_saldo
  16. rf_008_006 (5)
  17. rf_015_005 (6)
  18. rf_011_013 (7)
  19. cpayroll_trx
  20. mpayroll
  ... 379 variables en total


### `002_950_WorkFlow_01_senior`: Misma corrida que la anterior pero con el Feature Engineering Random Forest apagado, para determinar las ganancias obtenidas sin la utilización del mismo.
  * Semilla `163393`
  * Feature Engineering Random Forest desactivado.
* Ganancias obtenidas:
  * 61.427
  * 61.737
  * 60.877
  * 60.517
  * 60.107
* Conclusión: El Feature Engineering Random Forest aporta una mejora de entre 0.6 y ~1.7 puntos en la métrica de ganancia.

### `003_950_WorkFlow_01_senior`: Corrida con el Feature Engineering Random Forest activado, pero modificando los parámetros de `Num_iterations` y `Num_leaves` para determinar si estas variaciones aportan mayor ganancia. Semilla `163393`




## a