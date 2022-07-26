DO
$$
BEGIN
FOR i IN 1..200 LOOP
    INSERT INTO tbl_clients (
        name,
        email,
        birth_date,
        district,
        state,
        cpf_or_cnpj,
        cpf_cnpj,
        address,
        photo,
        rg,
        cep,
        cell_phone,
        phone,
        city
    ) VALUES (
        'William ' || i,
        'my-email@gmail.com' || i,
        '1990-11-09',
        'Centro',
        'SP',
        'cpf',
        '44444444444',
        'Rua XYZ',
        'images/upload/pPSojlIT_400x400_LOTGyMO.jpg',
        '5555555555'|| i,
        '16400035',
        '551499247'|| i,
        '55149924'|| i,
        'Lins'
    );
END LOOP;
END;
$$
;