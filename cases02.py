menu = int(input("informe um numero de 1 a 4 para escolher um compuatdor de sua prefência.\n"
" 1-PC GAMER "
" 2-PC ESCRITÓRIO "
" 3-PC SERVIDOR "
" 4-PC GAMER CUSTO BENEFICIO :"
))
match menu:
    case 1:
        print("PC GAMER" 
        "- processador ryzen 5600" 
        "- placa de video RTX 5090" 
        "- SSD NVMe 1 TB"
        "- 32gb RAM DDR4"
        "- FONTE 650w 80 plus bronze  ")
    case 2:
        print("PC ESCRITÓRIO" 
        "- intel core i3-14100" 
        "- SSD 512GB"
        "- 8gb RAM DDR4"
        "- FONTE 400w 80 plus  "
        "- placa mãe h610/b760")
    case 3:
        print("PC SERVIDOR" 
        "- intel Core i7" 
        "- SSD 512GB"
        "- 16gb RAM DDR4"
        "- FONTE 500w 80 plus  ")
    case 4:
        print("PC CUSTO BENEFICIO" 
        "- ADM RYZEN 5 5600" 
        "- SSD 512GB NVMe"
        "- 16gb RAM DDR4"
        "- FONTE 550w 80 plus  "
        "- placa mãe b550M")
    