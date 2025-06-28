document.addEventListener('DOMContentLoaded', function() {
    // Autofocus ke input nama
    var namaInput = document.querySelector('input[name="nama"]');
    if (namaInput) namaInput.focus();

    // Modal kirim pesan
    var form = document.querySelector('form[action="/"]');
    var popup = document.getElementById('popup-modal');
    var closeBtn = document.getElementById('close-popup');
    if (form && popup && closeBtn) {
        form.addEventListener('submit', function(e) {
            // e.preventDefault(); // Jika ingin popup sebelum submit, aktifkan ini
            // popup.classList.add('active');
        });
        closeBtn.addEventListener('click', function() {
            popup.classList.remove('active');
        });
    }

    // Modal konfirmasi hapus
    var hapusModal = document.getElementById('modal-hapus');
    var hapusText = document.getElementById('hapus-text');
    var hapusYa = document.getElementById('hapus-ya');
    var hapusTidak = document.getElementById('hapus-tidak');
    var closeHapus = document.getElementById('close-hapus');
    var formHapus = null;

    document.querySelectorAll('.btn-hapus').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var nama = btn.getAttribute('data-nama');
            hapusText.textContent = 'Yakin hapus pesan dari "' + nama + '"?';
            hapusModal.classList.add('active');
            formHapus = btn.closest('form');
        });
    });

    hapusYa && hapusYa.addEventListener('click', function() {
        if (formHapus) formHapus.submit();
        hapusModal.classList.remove('active');
    });

    hapusTidak && hapusTidak.addEventListener('click', function() {
        hapusModal.classList.remove('active');
        formHapus = null;
    });

    closeHapus && closeHapus.addEventListener('click', function() {
        hapusModal.classList.remove('active');
        formHapus = null;
    });
});