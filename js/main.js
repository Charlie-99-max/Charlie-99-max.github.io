(() => {
  'use strict';

  const header = document.querySelector('.site-header');
  const menuButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  const navLinks = [...document.querySelectorAll('.site-nav a[href^="#"]')];

  const closeMenu = () => {
    if (!menuButton || !nav) return;
    menuButton.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
  };

  menuButton?.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    nav?.classList.toggle('open', !isOpen);
  });

  navLinks.forEach((link) => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });

  const setHeaderState = () => header?.classList.toggle('scrolled', window.scrollY > 18);
  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });

  const revealItems = document.querySelectorAll('.reveal');
  revealItems.forEach((item) => {
    const delay = Number(item.dataset.delay || 0);
    item.style.setProperty('--delay', `${delay}ms`);
  });

  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -35px' });
    revealItems.forEach((item) => revealObserver.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('visible'));
  }

  const sections = document.querySelectorAll('main section[id]');
  if ('IntersectionObserver' in window && navLinks.length) {
    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        navLinks.forEach((link) => {
          link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
        });
      });
    }, { rootMargin: '-30% 0px -58%', threshold: 0 });
    sections.forEach((section) => sectionObserver.observe(section));
  }

  const translations = {
    navAbout: '关于', navResearch: '研究', navPublications: '论文', navPatents: '专利', navProjects: '项目', navCv: '简历', navContact: '联系',
    heroEyebrow: '清华大学 · 中国北京', heroRole: '机械工程博士研究生\n清华大学', heroFocus: '活体 DNA 数据存储',
    heroKeywords: '工程化活体材料 · 微流控 · 生物制造 · 自动化',
    heroStatement: '我致力于开发用于 DNA 数据存储、检索、再生、改写与自动化运行的工程化活体系统。',
    viewResearch: '探索研究', viewPublications: '代表论文', downloadCv: '下载中文简历',
    heroLab: '生物制造中心', heroDept: '清华大学机械工程系',
    aboutKicker: '个人简介', aboutTitle: '关于我',
    chainProblem: '科学问题', chainBio: '生物工程', chainMicro: '微流控', chainAuto: '自动化', chainSystem: '一体化系统',
    statPapers: '同行评议论文', statFirst: 'Advanced Materials 第一作者论文', statPatents: '专利及专利申请', statTalks: '口头报告',
    researchKicker: '研究方向', researchTitle: '研究兴趣', researchIntro: '从可编程细胞到一体化活体信息系统。',
    interestOne: '活体 DNA 数据存储', interestTwo: '工程化活体材料', interestThree: '微流控与生物制造', interestFour: '自动化与智能仪器',
    highlightsKicker: '代表性工作', highlightsTitle: '研究亮点', highlightsIntro: '三个项目构成了我的核心科研主线。',
    diskSubtitle: '一种可再生的活体 DNA 存储架构',
    diskBody: '该系统将冻干 Living Disk、荧光 Optical Retriever 与桌面级 Living Drive 连接为一体。检索得到的 ELMM 释放携带信息的细菌，细菌扩增后重新封装，用于补充原始数据库，推动活体 DNA 存储由静态保存走向可重复运行。',
    cyclesTen: '自动再生循环', cyclesThirteen: '冻干—复水循环', dryStorage: '已验证室温干态保存',
    elmmSubtitle: '面向随机访问活体 DNA 存储的物理文件架构',
    elmmBody: 'ELMM 将携带数据的工程菌、功能质粒与水凝胶微球集成为离散的活体文件单元。胞内荧光作为物理索引，支持文件级选择和布尔查询；冻干则实现紧凑的干态保存与后续恢复。',
    elmmPointOne: '物理化、文件级的活体存储单元', elmmPointTwo: '荧光辅助随机访问，实验分选准确率超过 98%', elmmPointThree: '完成 7 次冻干—复水循环验证',
    cancerSubtitle: '面向患者特异性肿瘤模型的微流控制造',
    cancerBody: '通过液滴微流控实现患者来源肺癌和胃癌类组装体的可控制造，用于肿瘤微环境建模与治疗药物筛选。',
    myContribution: '本人贡献', contributionBody: '微流控平台设计与制造工艺开发。',
    publicationsKicker: '学术成果', publicationsTitle: '代表性论文', viewAllPublications: '查看全部 6 篇论文 →',
    projectsKicker: '工程能力', projectsTitle: '代表性项目', projectsIntro: '核心科研主线之外的系统构建经验。', viewAllProjects: '查看全部 14 项项目 →',
    projectDna: '开发芯片式自动化 DNA 合成仪原型与协同编码方法，完成 13 nt DNA 合成验证。',
    projectVision: '构建图像预处理、特征提取与点阵识别 OpenCV 流程，并将核心模块封装为 DLL 以支持系统集成。',
    projectLaser: '设计动态聚焦机械系统与嵌入式伺服控制，集成 STM32、传感器、执行器、仿真与原型制造。',
    experienceKicker: '学术背景', educationTitle: '教育经历', phdDegree: '机械工程博士研究生 · 预计 2026 年 12 月毕业', phdDetails: '导师：熊卓教授 · GPA：3.8 / 4.0',
    bachelorDegree: '机械工程工学学士', bachelorDetails: 'GPA：3.77 / 4.0 · 专业排名：3 / 106',
    talksKicker: '学术交流', talksTitle: '代表性报告', moreKicker: '学术服务', moreTitle: '教学、奖励与专利', fullCv: '查看完整简历 →',
    teachingTitle: '教学', teachingAward: '清华大学优秀助教 · 前 5%', awardsTitle: '代表性奖励', patentsTitle: '专利',
    patentSummary: '6 项中国发明专利 / 申请', patentGranted: '3 项授权 · 1 项公开 · 2 项申请', patentStudent: '作为学生第一发明人参与 3 项 DNA 存储专利申请', viewPatents: '查看全部 6 项专利 →',
    mediaKicker: '社会传播', mediaTitle: '媒体与新闻', mediaIntro: '活体 DNA 存储研究的代表性报道。',
    skillsKicker: '方法能力', skillsTitle: '技术专长', contactKicker: '建立联系', contactTitle: '期待与您讨论研究。',
    contactBody: '欢迎就博士后机会、学术合作、活体 DNA 存储、生物制造与智能科研仪器开展交流。', contactAffiliation: '清华大学 · 中国北京'
  };

  const about = document.querySelector('[data-copy="aboutText"]');
  const aboutEnglish = about?.textContent.trim() || '';
  const aboutChinese = '骆浩是清华大学机械工程博士研究生，研究核心是如何将活体系统转化为可物理寻址、可再生的信息介质。他将 DNA 编码、质粒与工程菌设计、液滴微流控、水凝胶生物制造、干态保存、光学检索与科研自动化贯通起来。博士期间，他建立了工程化活体记忆微球（ELMM）这一文件级存储单元，实现活体 DNA 数据的随机访问；进一步发展出可再生 Living Disk–Drive 架构，支持释放、扩增、再封装、数据库补库与信息改写接口。除核心方向外，他还参与患者来源肿瘤类组装体研究，主要负责微流控平台设计与制造工艺开发。他的长期目标是将生物可编程性转化为可靠的一体化工程系统。';

  const languageButtons = document.querySelectorAll('[data-set-lang]');
  const applyLanguage = (language) => {
    const nextLanguage = language === 'zh' ? 'zh' : 'en';
    document.documentElement.lang = nextLanguage === 'zh' ? 'zh-CN' : 'en';
    document.body.classList.toggle('lang-zh', nextLanguage === 'zh');
    document.querySelectorAll('[data-i18n]').forEach((element) => {
      if (!element.dataset.en) element.dataset.en = element.textContent;
      const translated = nextLanguage === 'zh' ? translations[element.dataset.i18n] : element.dataset.en;
      if (translated) element.textContent = translated;
    });
    document.querySelectorAll('[data-zh], [data-zh-html]').forEach((element) => {
      if (!element.dataset.enLocalHtml) element.dataset.enLocalHtml = element.innerHTML;
      if (nextLanguage === 'zh') {
        if (element.dataset.zhHtml) element.innerHTML = element.dataset.zhHtml;
        else element.textContent = element.dataset.zh;
      } else {
        element.innerHTML = element.dataset.enLocalHtml;
      }
    });
    document.querySelectorAll('[data-lang-only]').forEach((element) => {
      element.hidden = element.dataset.langOnly !== nextLanguage;
    });
    document.querySelectorAll('[data-href-en][data-href-zh]').forEach((element) => {
      element.setAttribute('href', nextLanguage === 'zh' ? element.dataset.hrefZh : element.dataset.hrefEn);
    });
    if (document.body.dataset.titleEn && document.body.dataset.titleZh) {
      document.title = nextLanguage === 'zh' ? document.body.dataset.titleZh : document.body.dataset.titleEn;
    }
    const description = document.querySelector('meta[name="description"]');
    if (description && document.body.dataset.descriptionEn && document.body.dataset.descriptionZh) {
      description.content = nextLanguage === 'zh' ? document.body.dataset.descriptionZh : document.body.dataset.descriptionEn;
    }
    if (about) about.textContent = nextLanguage === 'zh' ? aboutChinese : aboutEnglish;
    languageButtons.forEach((button) => {
      const selected = button.dataset.setLang === nextLanguage;
      button.classList.toggle('active', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    try { localStorage.setItem('hao-luo-language', nextLanguage); } catch (_) { /* preference is optional */ }
  };

  languageButtons.forEach((button) => button.addEventListener('click', () => applyLanguage(button.dataset.setLang)));
  let initialLanguage = 'en';
  try { initialLanguage = localStorage.getItem('hao-luo-language') || 'en'; } catch (_) { /* use English */ }
  applyLanguage(initialLanguage);
})();
