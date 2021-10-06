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
        'my-email@gmail.com',
        '1990-11-09',
        'Centro',
        'SP',
        'cpf',
        '44444444444',
        'Rua XYZ',
        'images/upload/pPSojlIT_400x400_LOTGyMO.jpg',
        '55555555555',
        '16400035',
        '55149924792',
        '5514992479',
        'Lins'
    );
END LOOP;
END;
$$
;