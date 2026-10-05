class CancionManager:

    def __init__(self, db):
        self.db = db

    def get_all(self, año_min=None, año_max=None, genero=None):
        query = "SELECT * FROM canciones WHERE 1=1"
        params = []

        if año_min is not None:
            query += " AND año >= ?"
            params.append(año_min)

        if año_max is not None:
            query += " AND año <= ?"
            params.append(año_max)

        if genero is not None:
            query += " AND genero = ?"
            params.append(genero)

        cursor = self.db.execute(query, params)

        return cursor.fetchall()

    def get_by_id(self, id):
        cursor = self.db.execute(
            "SELECT * FROM canciones WHERE id = ?",
            (id,)
        )

        return cursor.fetchone()

    def create(self, data):
        cursor = self.db.execute(
            """
            INSERT INTO canciones
            (titulo, album, año, duracion, genero, popularidad)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                data.titulo,
                data.album,
                data.año,
                data.duracion,
                data.genero,
                data.popularidad
            )
        )

        self.db.commit()

        return self.get_by_id(cursor.lastrowid)

    def update(self, id, data):
        updates = data.model_dump(exclude_unset=True)

        fields = []
        params = []

        for field, value in updates.items():
            fields.append(f"{field} = ?")
            params.append(value)

        if not fields:
            return self.get_by_id(id)

        params.append(id)

        query = f"""
            UPDATE canciones
            SET {", ".join(fields)}
            WHERE id = ?
        """

        self.db.execute(query, params)
        self.db.commit()

        return self.get_by_id(id)

    def delete(self, id):
        cursor = self.db.execute(
            "DELETE FROM canciones WHERE id = ?",
            (id,)
        )

        self.db.commit()

        return cursor.rowcount