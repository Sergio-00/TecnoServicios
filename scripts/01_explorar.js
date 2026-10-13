db = db.getSiblingDB("tecnoservicios_lab");

if (db.ordenes_demo.countDocuments({ _id: "OS-DEMO-001" }) === 0) {
  db.ordenes_demo.insertOne({
    _id: "OS-DEMO-001",
    cliente_alias: "Cliente ficticio 01",
    equipo: {
      codigo: "EQ-DEMO-001",
      tipo: "portatil",
      accesorios_recibidos: ["cargador", "estuche"],
    },
    falla_reportada: "No enciende",
    prioridad: "alta",
    estado: "recibida",
    requiere_diagnostico: true,
    fecha_ingreso: new Date("2026-10-06T13:00:00Z"),
  });
}

printjson(db.ordenes_demo.findOne({ _id: "OS-DEMO-001" }));
print(db.ordenes_demo.countDocuments({ _id: "OS-DEMO-001" }));

const orden = db.ordenes_demo.findOne({ _id: "OS-DEMO-001" });
print(orden.fecha_ingreso instanceof Date);

if (db.ordenes_demo.countDocuments({ _id: "OS-DEMO-002" }) === 0) {
  db.ordenes_demo.insertOne({
    _id: "OS-DEMO-002",
    cliente_alias: "Cliente ficticio 01",
    equipo: {
      codigo: "EQ-DEMO-002",
      tipo: "telefono",
      accesorios_recibidos: [],
    },
    falla_reportada: "Pantalla sin respuesta",
    prioridad: "alta",
    estado: "recibida",
    requiere_diagnostico: true,
    fecha_ingreso: new Date(),
  });
}

print(db.ordenes_demo.countDocuments({ _id: "OS-DEMO-002" }));
