-- Create the database (run this command in psql or pgAdmin)
CREATE DATABASE financial_dashboard;

-- Connect to the database
\c financial_dashboard

-- Create the transactions table
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    tanggal DATE NOT NULL,
    keterangan VARCHAR(255) NOT NULL,
    debit NUMERIC(15, 2),
    kredit NUMERIC(15, 2),
    saldo NUMERIC(15, 2) NOT NULL
);

-- Create an index on the tanggal column for faster queries
CREATE INDEX idx_transactions_tanggal ON transactions(tanggal);

-- Insert some sample data
INSERT INTO transactions (tanggal, keterangan, debit, kredit, saldo) VALUES
    ('2024-01-02', 'Saldo awal', 5500000.00, NULL, 5500000.00),
    ('2024-01-03', 'Pembayaran listrik', NULL, 500000.00, 5000000.00),
    ('2024-01-05', 'Penjualan produk', 2000000.00, NULL, 7000000.00),
    ('2024-01-10', 'Pembayaran gaji karyawan', NULL, 3000000.00, 4000000.00),
    ('2024-01-15', 'Pembelian bahan baku', NULL, 1500000.00, 2500000.00),
    ('2024-01-20', 'Penjualan jasa', 3000000.00, NULL, 5500000.00),
    ('2024-01-25', 'Pembayaran sewa kantor', NULL, 2000000.00, 3500000.00),
    ('2024-01-31', 'Penerimaan piutang', 1500000.00, NULL, 5000000.00);

-- Verify the data
SELECT * FROM transactions ORDER BY tanggal;
