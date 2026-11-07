
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BOX NO1 KAISER</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:Arial,sans-serif;background:#080a0d;color:#f5f5f5}
:root{--lime:#c7ff35;--dark:#10151a}
a{text-decoration:none;color:inherit}
.nav{position:sticky;top:0;z-index:99;background:#080a0dee;
border-bottom:1px solid #c7ff3533;backdrop-filter:blur(15px)}
.nav-inner{max-width:1150px;margin:auto;padding:16px 22px;
display:flex;align-items:center;justify-content:space-between;gap:20px}
.brand{font-weight:900;letter-spacing:2px;color:var(--lime)}
.brand-mark{background:var(--lime);color:#080a0d;padding:9px;border-radius:8px;margin-right:8px}
.nav-links{display:flex;gap:18px;flex-wrap:wrap;font-size:12px}
.nav-links a:hover{color:var(--lime)}
.btn{display:inline-block;background:var(--lime);color:#080a0d;
padding:13px 20px;border-radius:7px;font-weight:900;font-size:12px;
transition:.25s;border:1px solid var(--lime)}
.btn:hover{transform:translateY(-3px);box-shadow:0 0 25px #c7ff3580}
.btn.outline{background:transparent;color:var(--lime)}
.hero{min-height:700px;display:flex;align-items:center;justify-content:center;
text-align:center;padding:90px 20px;position:relative;overflow:hidden;
background:linear-gradient(90deg,#05070bf2,#05070b99),
url('https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1800&q=90') center/cover}
.hero:after{content:"";position:absolute;inset:0;
background:radial-gradient(circle at center,#c7ff3517,transparent 65%);pointer-events:none}
.hero-content{position:relative;z-index:1;max-width:850px}
.eyebrow{color:var(--lime);letter-spacing:4px;font-size:11px;font-weight:bold}
.logo{width:145px;height:145px;object-fit:cover;border-radius:50%;
border:3px solid var(--lime);padding:5px;margin:28px auto;
box-shadow:0 0 35px #c7ff3570;display:block}
h1{font-size:clamp(38px,8vw,78px);font-weight:1000;letter-spacing:-2px}
h1 span{display:block;color:var(--lime);font-size:15px;letter-spacing:6px;margin-top:15px}
.hero p{color:#c6cbd0;line-height:1.9;max-width:700px;margin:25px auto}
.actions{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:25px}
.stats{display:flex;justify-content:center;gap:45px;margin-top:55px;flex-wrap:wrap}
.stat strong{display:block;color:var(--lime);font-size:24px}
.stat small{font-size:10px;color:#aaa;letter-spacing:2px}
.section{padding:85px 20px}
.container{max-width:1100px;margin:auto}
.heading{text-align:center;margin-bottom:40px}
.heading small{color:var(--lime);letter-spacing:4px;font-weight:bold}
.heading h2{font-size:clamp(25px,5vw,40px);margin:13px 0}
.heading p{color:#999;line-height:1.8;max-width:700px;margin:auto}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:linear-gradient(145deg,#171d22,#0d1014);
border:1px solid #ffffff12;padding:28px;border-radius:13px;
transition:.3s;position:relative;overflow:hidden}
.card:hover{transform:translateY(-6px);border-color:var(--lime);
box-shadow:0 10px 35px #000}
.card .number{color:var(--lime);font-size:12px;letter-spacing:3px}
.card .symbol{font-size:35px;margin:22px 0}
.card h3{margin-bottom:12px}
.card p{color:#999;line-height:1.8;font-size:14px}
.dark{background:#0d1115}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}
.gallery img{width:100%;height:220px;object-fit:cover;border-radius:12px;
border:1px solid #ffffff20;transition:.3s}
.gallery img:hover{transform:scale(1.025);border-color:var(--lime)}
.pricing{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;max-width:750px;margin:auto}
.price-card{background:#12171c;border:1px solid #c7ff3540;
border-radius:15px;padding:35px;text-align:center}
.price-card h3{color:var(--lime);letter-spacing:3px}
.price{font-size:65px;font-weight:900;margin:20px}
.price small{font-size:14px;color:#aaa}
.price-card p{color:#aaa;margin-bottom:25px;line-height:1.8}
.people{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;max-width:750px;margin:auto}
.person{display:flex;align-items:center;gap:20px;padding:25px;
background:#12171c;border:1px solid #ffffff18;border-radius:12px}
.person-icon{width:55px;height:55px;border-radius:50%;display:grid;
place-items:center;background:#c7ff3520;color:var(--lime);font-size:25px}
.person small{color:var(--lime);letter-spacing:2px}
.person h3{margin-top:7px}
.rules{max-width:800px;margin:auto;display:grid;gap:12px}
.rule{background:#12171c;border:1px solid #ffffff12;
padding:18px;border-radius:9px;color:#ccc;line-height:1.7}
.rule b{color:var(--lime);margin-right:12px}
.faq{max-width:800px;margin:auto}
details{background:#12171c;border:1px solid #ffffff15;
padding:20px;border-radius:9px;margin:12px 0}
summary{cursor:pointer;font-weight:bold}
details p{color:#aaa;line-height:1.8;margin-top:15px}
.join-box{text-align:center;background:linear-gradient(130deg,#202b12,#10151a);
border:1px solid #c7ff3555;padding:55px 25px;border-radius:18px}
.join-box p{color:#bbb;line-height:1.9;margin:18px auto;max-width:650px}
footer{padding:30px 20px;border-top:1px solid #ffffff15;text-align:center;
color:#777;font-size:12px;line-height:2}
@media(max-width:760px){
.nav-inner{flex-wrap:wrap}
.nav-links{order:3;width:100%;justify-content:center}
.grid{grid-template-columns:1fr}
.gallery{grid-template-columns:repeat(2,1fr)}
.gallery img{height:145px}
.stats{gap:25px}
.people,.pricing{grid-template-columns:1fr}
.hero{min-height:650px}
}
</style>
</head>
<body>

<script>
/* ===== CÀI ĐẶT WEBSITE ===== */
const LOGO_URL = "https://i.ibb.co/3KYbNxv/logo-xiud.jpg";
const DISCORD_URL = "https://discord.gg/W7MgFazWm";
/* ========================== */
</script>

<header class="nav">
<div class="nav-inner">
<a class="brand" href="#top"><span class="brand-mark">N1K</span> NO1 KAISER</a>
<nav class="nav-links">
<a href="#about">GIỚI THIỆU</a>
<a href="#activities">HOẠT ĐỘNG</a>
<a href="#test">ĐĂNG KÝ TEST</a>
<a href="#gallery">HÌNH ẢNH</a>
<a href="#team">QUẢN TRỊ</a>
<a href="#rules">NỘI QUY</a>
</nav>
<a class="btn discord" href="#join">DISCORD ↗</a>
</div>
</header>

<main id="top">
<section class="hero" id="about">
<div class="hero-content">
<div class="eyebrow">✦ OFFICIAL FREE FIRE COMMUNITY ✦</div>
<img class="logo" id="mainLogo" alt="BOX NO1 KAISER">
<h1>BOX NO1 KAISER
<span>BUILT BY THE COMMUNITY</span></h1>
<p>
Chào mừng bạn đến với BOX NO1 KAISER! Đây là nơi hội tụ những thành viên
yêu thích Free Fire, cùng giao lưu, kết nối, tìm kiếm đồng đội và tham gia
những trận đấu đầy thử thách. Chúng tôi hướng đến một cộng đồng năng động,
văn minh, đoàn kết và luôn có những hoạt động thú vị.
</p>
<div class="actions">
<a class="btn discord" href="#join">THAM GIA DISCORD ↗</a>
<a class="btn outline" href="#activities">KHÁM PHÁ KAISER ↓</a>
</div>
<div class="stats">
<div class="stat"><strong>NO.01</strong><small>KAISER COMMUNITY</small></div>
<div class="stat"><strong>KAI / HS</strong><small>HOẠT ĐỘNG CHÍNH</small></div>
<div class="stat"><strong>OPEN</strong><small>KẾT NỐI ANH EM</small></div>
</div>
</div>
</section>

<section class="section" id="activities">
<div class="container">
<div class="heading">
<small>DISCOVER KAISER</small>
<h2>KHÁM PHÁ CỘNG ĐỒNG</h2>
<p>Nhiều hoạt động dành cho thành viên, từ giao lưu đến thử thách kỹ năng và kết nối đồng đội.</p>
</div>
<div class="grid">
<article class="card"><div class="number">01 / KAI ROOM</div><div class="symbol">🎯</div><h3>PHÒNG KAI</h3><p>Giao lưu, thử thách kỹ năng và cùng anh em tạo nên những trận Kai sôi động.</p></article>
<article class="card"><div class="number">02 / HEADSHOT</div><div class="symbol">⚡</div><h3>PHÒNG HS</h3><p>Không gian thử thách khả năng ngắm bắn, phản xạ và tinh thần thi đấu.</p></article>
<article class="card"><div class="number">03 / TEAM UP</div><div class="symbol">🤝</div><h3>TÌM ĐỒNG ĐỘI</h3><p>Kết nối thành viên mới, tìm người chơi cùng và xây dựng những đội hình ăn ý.</p></article>
<article class="card"><div class="number">04 / COMMUNITY</div><div class="symbol">👑</div><h3>CỘNG ĐỒNG</h3><p>Trò chuyện, làm quen, chia sẻ những khoảnh khắc đáng nhớ cùng Kaiser.</p></article>
<article class="card"><div class="number">05 / EVENTS</div><div class="symbol">🏆</div><h3>SỰ KIỆN</h3><p>Cập nhật các hoạt động, thử thách và chương trình giao lưu của box.</p></article>
<article class="card"><div class="number">06 / SUPPORT</div><div class="symbol">🛡️</div><h3>HỖ TRỢ</h3><p>Đội ngũ quản trị hướng dẫn thành viên mới và giải đáp những thắc mắc.</p></article>
</div>
</div>
</section>

<section class="section dark" id="gallery">
<div class="container">
<div class="heading"><small>KAISER MOMENTS</small><h2>KHÔNG GIAN GAMING</h2><p>Một góc hình ảnh mang phong cách gaming của cộng đồng.</p></div>
<div class="gallery">
<img loading="lazy" src="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=700&q=85" alt="Gaming">
<img loading="lazy" src="https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=700&q=85" alt="Gaming setup">
<img loading="lazy" src="https://images.unsplash.com/photo-1593305841991-05c297ba4575?auto=format&fit=crop&w=700&q=85" alt="Thiết bị gaming">
</div>
</div>
</section>

<section class="section" id="test">
<div class="container">
<div class="heading"><small>JOIN THE TRYOUT</small><h2>ĐĂNG KÝ TEST PHÒNG KAI</h2>
<p>Muốn tham gia thử thách? Xem mức test và vào Discord để liên hệ đội ngũ quản trị.</p></div>
<div class="pricing">
<article class="price-card"><h3>✦ TEST NỮ</h3><div class="price">3 <small>lượt/chạm</small></div><p>Liên hệ quản trị viên trên Discord để đăng ký và xác nhận lịch test.</p><a class="btn discord" href="#join">ĐĂNG KÝ DISCORD ↗</a></article>
<article class="price-card"><h3>♛ TEST NAM</h3><div class="price">5 <small>lượt/chạm</small></div><p>Liên hệ quản trị viên trên Discord để đăng ký và xác nhận lịch test.</p><a class="btn discord" href="#join">ĐĂNG KÝ DISCORD ↗</a></article>
</div>
</div>
</section>

<section class="section dark" id="team">
<div class="container">
<div class="heading"><small>THE PEOPLE BEHIND KAISER</small><h2>BAN QUẢN TRỊ</h2><p>Những người phụ trách hỗ trợ và xây dựng hoạt động cộng đồng.</p></div>
<div class="people">
<div class="person"><div class="person-icon">♛</div><div><small>CHỦ BOX</small><h3>HỮU TRÍ</h3></div></div>
<div class="person"><div class="person-icon">✦</div><div><small>QUẢN TRỊ VIÊN</small><h3>QUỲNH ANH</h3></div></div>
</div>
</div>
</section>

<section class="section" id="rules">
<div class="container">
<div class="heading"><small>COMMUNITY GUIDELINES</small><h2>NỘI QUY KAISER</h2><p>Cùng nhau giữ môi trường giao lưu tích cực và tôn trọng mọi thành viên.</p></div>
<div class="rules">
<div class="rule"><b>01</b>Tôn trọng chủ box, quản trị viên và tất cả thành viên.</div>
<div class="rule"><b>02</b>Không spam, quảng cáo hoặc gây ảnh hưởng đến hoạt động chung.</div>
<div class="rule"><b>03</b>Không xúc phạm, quấy rối hay cố ý gây mâu thuẫn.</div>
<div class="rule"><b>04</b>Giao lưu phòng Kai và HS với tinh thần vui vẻ, chơi đẹp.</div>
<div class="rule"><b>05</b>Tuân thủ hướng dẫn hợp lý của đội ngũ quản trị.</div>
<div class="rule"><b>06</b>Giữ gìn hình ảnh và tinh thần cộng đồng BOX NO1 KAISER.</div>
</div>
</div>
</section>

<section class="section dark" id="faq">
<div class="container">
<div class="heading"><small>HELP CENTER</small><h2>CÂU HỎI THƯỜNG GẶP</h2></div>
<div class="faq">
<details><summary>Làm sao để tham gia BOX NO1 KAISER?</summary><p>Nhấn nút Discord trên website để vào máy chủ cộng đồng.</p></details>
<details><summary>Muốn đăng ký test phòng Kai thì làm sao?</summary><p>Vào Discord và liên hệ đội ngũ quản trị để được hướng dẫn.</p></details>
<details><summary>Mức test hiện tại là bao nhiêu?</summary><p>Test nữ: 3 lượt/chạm. Test nam: 5 lượt/chạm. Vui lòng xác nhận lại lịch với quản trị viên.</p></details>
<details><summary>Ai phụ trách cộng đồng?</summary><p>Chủ box: Hữu Trí. Quản trị viên: Quỳnh Anh.</p></details>
</div>
</div>
</section>

<section class="section" id="join">
<div class="container">
<div class="join-box">
<div class="eyebrow">BECOME A PART OF KAISER</div>
<h2 style="font-size:35px;margin-top:15px">SẴN SÀNG GIA NHẬP?</h2>
<p>Tham gia BOX NO1 KAISER để kết nối với cộng đồng, tìm đồng đội, cập nhật hoạt động và đăng ký test phòng Kai. Hãy cùng nhau tạo nên một cộng đồng Free Fire đoàn kết và chất lượng!</p>
<a class="btn discord" href="#" id="discordButton">THAM GIA DISCORD NGAY ↗</a>
</div>
</div>
</section>
</main>

<footer>
© 2026 BOX NO1 KAISER · KAISER COMMUNITY<br>
CHỦ BOX: HỮU TRÍ · QUẢN TRỊ: QUỲNH ANH<br>
PLAY FAIR · RESPECT EVERYONE · STAY KAISER
</footer>

<script>
document.getElementById("mainLogo").src = LOGO_URL;

function openDiscord(event){
  if(!DISCORD_URL || DISCORD_URL.includes("DAN_LINK_")){
    event.preventDefault();
    alert("Vui lòng thêm link mời Discord vào biến DISCORD_URL ở đầu file HTML.");
    return;
  }
  event.currentTarget.href = DISCORD_URL;
  event.currentTarget.target = "_blank";
}
document.querySelectorAll(".discord").forEach(button=>{
  button.addEventListener("click",openDiscord);
});
document.getElementById("discordButton").addEventListener("click",openDiscord);
</script>
</body>
</html>
