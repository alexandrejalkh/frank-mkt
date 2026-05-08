---
name: metricas-marketing
description: "KPIs marketing — ULTIMA skill bloco Marketing & Estrategia (apos posicionamento+branding+funil+big-idea). **CAC + LTV + LTV:CAC ratio**: B2B SaaS CAC $200-500 typical (industry-wide $1.200); ecommerce $20-60; LTV:CAC **3:1+ healthy** (<3 unsustainable, >5 underinvest growth); **CAC payback <12 meses healthy** (<80 dias best-in-class top performers). **ROAS**: 3-5x healthy generic; Meta Ads median **1.93x / avg 2.79x** (2026); email **6-10x**; social ads 3-5x; search 4-8x. **Marketing budget allocation**: B2C 5-10% revenue / B2B 2-5% / SaaS 8-15% (**median 8% 2026 down from 10%**). **Rule of 40 SaaS** (Brad Feld 2015): revenue growth + profit margin ≥40%; **SaaS Metrics Standards Board recommends ARR growth + FCF margin**; companies clearing R40 trade at **4.8x EV/Revenue median vs 2.7x fail = 74% premium**. **Magic Number** (Scale Venture Partners) = (Q ARR - prev Q ARR) × 4 / prev Q S&M spend; **>0.75 = healthy** investment efficiency. **Vanity vs Actionable metrics**: 'So What?' test rigoroso; vanity (followers, page views, likes, impressions) vs actionable (conversion rate per stage, CAC by source, retention cohort, ARPU lift). **Marketing attribution 2026**: multi-touch + last-touch dual-model **operating norm 2026**; W-shaped 30/30/30/10; **data-driven attribution requires 300-400 conversions/mês GA4**; **MMM (Marketing Mix Modeling) adoption tripled 9%→26%** driven by signal-loss + privacy + Google open-source MMM; iOS 14.5 + Chrome cookies = MTA coverage shrunk **30-60% of 2020 signal**. **Brand health 5 dimensions**: awareness depth + consideration + preference + emotional connection + advocacy; NPS + sentiment + recall (aided/unaided) + market share. **Conversion benchmarks 2026**: website 2-3% / ecommerce 1.5-3% / B2B 2.5-5% / SaaS free trial 3-7%. **Tools**: Looker Studio free + Geckoboard TV displays $31-149/mês + GA4 + HubSpot/Salesforce attribution + Mixpanel/Amplitude product analytics + Sprout Social brand health. Anti-patterns: vanity-first reporting, single-touch attribution last-touch only, Rule of 40 ignored, NPS sole brand metric, no measurement plan, ROAS without LTV context."
user-invocable: false
last_verified: 2026-05-08
next_review: 2026-11-08
volatility: medium
regrounding_sources:
  - "https://www.1clickreport.com/blog/marketing-kpi-benchmarks-industry-2026"
  - "https://aventis-advisors.com/rule-of-40-in-saas-2026/"
  - "https://userpilot.com/blog/vanity-metrics-vs-actionable-metrics-saas/"
  - "https://improvado.io/blog/multi-touch-attribution"
  - "https://sproutsocial.com/insights/brand-health-tracking/"
  - "https://www.growthspreeofficial.com/blogs/ltv-cac-ratio-b2b-saas-benchmarks-2026"
---

# Skill: metricas-marketing

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-08 | Proxima revisao: 2026-11-08 | Volatility: **medium** (6 meses)
> Frameworks (LTV:CAC, Rule of 40, Magic Number, vanity vs actionable) estaveis decadas. Benchmarks (CAC $200-500 SaaS, LTV:CAC 3:1, R40 4.8x EV/Rev premium) atualizam moderadamente. Privacy regulations (iOS 14.5, Chrome cookies) shifting attribution rapidly. **Re-validar semestralmente:**
> - 1ClickReport — KPI Benchmarks 2026 — https://www.1clickreport.com/blog/marketing-kpi-benchmarks-industry-2026
> - Aventis — Rule of 40 SaaS 2026 — https://aventis-advisors.com/rule-of-40-in-saas-2026/
> - Userpilot — Vanity vs Actionable — https://userpilot.com/blog/vanity-metrics-vs-actionable-metrics-saas/
> - Improvado — Multi-Touch Attribution 2026 — https://improvado.io/blog/multi-touch-attribution
> - Sprout Social — Brand Health Tracking 2026 — https://sproutsocial.com/insights/brand-health-tracking/
> - Growthspree — LTV:CAC B2B SaaS 2026 — https://www.growthspreeofficial.com/blogs/ltv-cac-ratio-b2b-saas-benchmarks-2026
>
> **Acionamento:** definir KPIs marketing; CAC/LTV calculation; ROAS analysis; Rule of 40 SaaS audit; Magic Number quarterly; vanity vs actionable distinction; attribution model decision; brand health tracking; benchmark comparison industry; dashboard setup; measurement plan campanha; marketing budget allocation.
> **Skills relacionadas:** `posicionamento-marca` + `branding` + `funil-jornada` + `big-idea` (anteriores Marketing & Estrategia bloco), `escrita-por-publico` (B2B vs B2C metrics), `multi-platform-narrative` (cross-platform ROI), `engajamento-comunidade` Sec 7 (CLG metrics), `seo-fundamentos` Sec 12 (SEO KPIs), `linkedin-ads` + `instagram-ads` + `facebook-ads` + `tiktok-criativo` (per-platform ad metrics).
> **Pre-requisito:** posicionamento + branding + funil + big-idea definidos; data infrastructure minima (GA4 free + 1 product analytics tool + CRM se B2B); finance team alignment; quarterly review cadence committed.

---

## 1. Visao Geral

Metricas Marketing = como **provar valor** + **diagnosticar problemas** + **alocar budget** baseado em data. Skill final do bloco Marketing & Estrategia — fecha cycle posicionamento → branding → funil → big-idea → MEDIR effectiveness. **Vanity metrics** (followers, page views, likes) **misleading** em 2026 — actionable metrics (conversion per stage, CAC by source, retention cohort, ARPU lift) win.

Esta skill cobre 7 fundacoes:

1. **CAC + LTV + LTV:CAC ratio** + benchmarks 2026.
2. **ROAS** + benchmarks per channel.
3. **Rule of 40 SaaS** + Magic Number formulas.
4. **Vanity vs Actionable** — "So What?" test.
5. **Marketing attribution** — multi-touch + MMM 2026 shift.
6. **Brand health 5 dimensions** + tracking.
7. **Marketing dashboards** — Looker Studio + Geckoboard.

Mais 1 aplicacao:

8. **Brazil-specific metrics** — Pix conversion + WhatsApp engagement + Mercado Livre.

### 1.1 Acionamento

| Gatilho | Exemplo |
|---------|---------|
| Define marketing KPIs | "Quais KPIs measure performance?" |
| CAC analysis | "CAC subindo — diagnostic?" |
| LTV calculation | "LTV correto?" |
| LTV:CAC audit | "Healthy ratio?" |
| ROAS per channel | "Email vs Meta vs Google ROAS?" |
| Rule of 40 SaaS | "R40 score audit?" |
| Magic Number | "S&M efficiency calc?" |
| Vanity metrics fix | "Diretor reporta followers — actionable?" |
| Attribution model | "Last-touch suficiente?" |
| Brand health setup | "Tracker brand health monthly?" |
| Dashboard build | "Looker vs Geckoboard?" |
| Budget allocation | "Quanto investir marketing?" |
| Conversion benchmarks | "Conversion rate normal?" |

### 1.2 Pre-requisitos

- [ ] **`posicionamento-marca` + `branding` + `funil-jornada` + `big-idea` definidos** (foundation strategy).
- [ ] **Data infrastructure** — GA4 free + 1 product analytics + CRM se B2B.
- [ ] **Finance team alignment** (CFO/Controller buy-in).
- [ ] **Quarterly review cadence** committed.
- [ ] **Stakeholders aligned** (founder/CMO/CFO).

> **Cristal C0 — NAO CHUTAR.** Vanity metrics (followers, page views) sem context = misleading. ROAS sem LTV = short-termism. Single-touch attribution last-touch only = misattribution 60%+ pipeline. Re-validar com finance team + cohort analysis (NÃO point-in-time) + benchmark comparison industry.

---

## 2. Cenario 2026 — efficient growth + privacy-first attribution

### 2.1 Stats fundamentais 2026

```
EFFICIENT GROWTH ERA
   2010-2022: "growth at all costs" (Uber/WeWork)
   2023-2026: "efficient growth" (R40 + Magic Number priority)

   Investors fund efficient growth (cf. `escrita-por-publico` Sec 6)
   = unit economics = primary KPIs
   = vanity metrics = penalized

PRIVACY-FIRST ATTRIBUTION
   iOS 14.5 (Apr 2021): App Tracking Transparency
   Chrome 3rd-party cookies deprecated (in progress)
   GDPR + CCPA + LGPD enforcement

   IMPACT
   - MTA (Multi-Touch Attribution) coverage shrunk
     30-60% of 2020 signal
   - MMM (Marketing Mix Modeling) adoption tripled
     9% → 26% over 3 years
   - Google open-sourced MMM library (2024)
   - Server-side tracking (CAPI) mandatory

AI-DRIVEN ATTRIBUTION
   GA4 data-driven attribution (default)
   Requires 300-400 conversions/mês
   Below = rule-based fallback
```

### 2.2 'MQL is dead' shift (cf. `funil-jornada` Sec 2.2)

```
2026 PRIMARY KPIs (marketing)

WAS (2010s legacy)
   - MQLs (Marketing Qualified Leads)
   - Page views
   - Social followers
   - Email open rate

NOW (2026)
   - SQLs (Sales Qualified Leads)
   - Pipeline created (revenue-weighted)
   - CAC payback period
   - NRR (Net Revenue Retention)
   - LTV:CAC ratio
   - Magic Number (SaaS)
   - Rule of 40 (SaaS)
```

### 2.3 Marketing budget 2026

```
PERCENTAGE OF REVENUE TYPICAL

B2C consumer brands: 5-10%
B2B services/products: 2-5%
SaaS B2B: 8-15% (median 8% 2026 down from 10% legacy)
DTC ecommerce: 10-20%
Enterprise B2B: 2-4%

ALLOCATION WITHIN MARKETING BUDGET
   Paid ads: 30-50%
   Content + SEO: 15-25%
   Events + sponsorships: 10-20% (B2B higher)
   Tools + software: 5-10%
   Salaries + agencies: bulk (often >50% if in-house)
   Brand building: 10-25%
   Performance: 50-75%
```

---

## 3. CAC + LTV + LTV:CAC ratio

### 3.1 CAC (Customer Acquisition Cost)

```
DEFINITION
   Total marketing + sales spend / new customers acquired

FORMULA
   CAC = (Marketing $ + Sales $) / # New Customers

INCLUDE IN CAC
   - Ads (paid media)
   - Content production
   - SEO tools + content
   - Email tools
   - CRM costs
   - Marketing team salaries (loaded)
   - Sales team salaries (loaded)
   - Sales tools (CRM, sales engagement)

EXCLUDE FROM CAC
   - Customer success post-purchase
   - Product development
   - General + administrative
```

### 3.2 CAC benchmarks 2026

```
BY INDUSTRY/MODEL

B2B SaaS
   Industry-wide average: $1,200
   Healthy range: $200-500 (mid-market)
   Enterprise: $5,000-50,000 (high-touch)
   Channel breakdown:
   - Organic search: $480-942 (best)
   - Paid search: $802
   - Social ads: variable

E-COMMERCE
   $20-60 typical
   Premium DTC: $50-150
   Mass market: $10-30

LOCAL SERVICES
   $50-150 typical

ENTERPRISE B2B
   $5,000-50,000
   Multi-touch + sales-heavy

BY ACQUISITION CHANNEL
   - Organic SEO: lowest CAC
   - Email (existing list): low
   - Referrals: low
   - Content marketing: medium
   - Paid social: medium-high
   - Paid search: medium-high
   - Outbound sales: high
   - Events/conferences: high
```

### 3.3 CAC Payback Period

```
CAC PAYBACK = Time to recover CAC via gross margin

FORMULA
   CAC Payback (months) = CAC / (MRR × Gross Margin)

BENCHMARKS B2B SaaS
   Best-in-class: <12 months (top performers <80 days)
   Healthy: 12-18 months
   Concerning: 18-24 months
   Bad: >24 months

LOWER PAYBACK = BETTER
   Faster cash recycle
   Less capital required to grow
   Lower risk
```

### 3.4 LTV (Customer Lifetime Value)

```
DEFINITION
   Total revenue per customer over their lifetime

FORMULA SIMPLE
   LTV = ARPU × Avg Lifespan × Gross Margin

FORMULA COMPLEX
   LTV = (Avg Order Value × Purchase Frequency × Customer Lifespan) × Gross Margin

EXAMPLE B2B SaaS
   ARPU: $500/month
   Lifespan: 3 years (36 months)
   Gross Margin: 75%
   LTV = $500 × 36 × 0.75 = $13,500

EXAMPLE ECOMMERCE
   AOV: $80
   Frequency: 3x/year
   Lifespan: 2 years
   Gross Margin: 40%
   LTV = $80 × 3 × 2 × 0.40 = $192

CAVEATS
   - Predictive (estimates future)
   - Cohort-based ideal (vs blanket)
   - Churn varies = LTV varies
   - Should refresh quarterly
```

### 3.5 LTV:CAC ratio

```
HEALTHIEST PREDICATOR UNIT ECONOMICS

FORMULA
   LTV:CAC = LTV / CAC

BENCHMARKS
   <1:1   = Bad (losing money each customer)
   1-3:1  = Concerning (sustainable but barely)
   3:1    = Healthy minimum (industry standard)
   3-5:1  = Excellent
   >5:1   = Underinvesting growth (could spend more)

INTERPRETATION
   3:1 means each $1 CAC returns $3 LTV
   = 200% return per customer (gross margin terms)

WHY 3:1 MIN
   Account for fixed costs + R&D + G&A + risk + churn
   3x LTV needed to fund operations + grow

ABOVE 5:1 = OPPORTUNITY
   Could increase CAC investment
   Capture more market share
   Spend more aggressive growth
```

---

## 4. ROAS (Return on Ad Spend)

### 4.1 ROAS formula + benchmarks

```
FORMULA
   ROAS = Revenue from Ads / Ad Spend

BENCHMARKS PER CHANNEL 2026

EMAIL MARKETING
   6-10x ROAS (best channel)
   = $1 spent → $6-10 revenue

SEARCH ADS (Google/Bing)
   4-8x ROAS
   High intent buyers

SOCIAL ADS (Meta/IG/FB)
   3-5x ROAS
   Median Meta 2026: 1.93x
   Average Meta: 2.79x
   (Cf. `instagram-ads` + `facebook-ads`)

DISPLAY ADS
   2-4x ROAS
   Lower intent

VIDEO ADS (YouTube/TikTok)
   2-5x ROAS
   Brand awareness + conversion mix

GENERAL HEALTH RANGE
   3-5x = healthy most industries
   <3x = unprofitable typically (depends LTV)
   >5x = excellent
```

### 4.2 ROAS vs LTV-based ROAS

```
CRITICAL DISTINCTION

SHORT-TERM ROAS (transactional)
   Revenue = first purchase only
   Misses retention + LTV
   Underestimates ad value if high LTV product

LTV-BASED ROAS (long-term)
   Revenue = LTV (full customer lifetime)
   = TRUE economic return ad spend
   Especially important B2B SaaS + subscription

EXAMPLE
   $1 ad spend → $5 first purchase → $50 LTV
   Short-term ROAS: 5x
   LTV-based ROAS: 50x
   = decision: invest more (LTV justifies)
```

### 4.3 Channel-specific nuances

```
EMAIL (highest ROAS)
   Owned audience (lower CAC effective)
   But: list-building cost not in ROAS
   Real ROAS = email + acquisition cost

SEARCH (high intent + high CAC)
   Bottom-of-funnel
   High conversion rate but premium CPC

SOCIAL (top + mid funnel)
   Lower direct ROAS but assists conversion
   Multi-touch attribution captures better
   (Cf. Sec 5)

VIDEO (brand + conversion)
   Best for awareness lift + brand recall
   ROAS underestimates true value
```

### 4.4 ROAS targets by company stage

```
EARLY-STAGE STARTUP
   ROAS: 1.5-3x acceptable (testing + iterating)
   Focus: learning > efficiency
   Goal: find PMF channels

GROWTH-STAGE
   ROAS: 3-5x target
   Focus: scale winning channels
   Goal: efficient growth

MATURE
   ROAS: 4-8x typical
   Focus: optimization + diversification
   Goal: sustainable expansion

DECLINING
   ROAS focus may indicate over-optimization
   Consider brand investment (brand health)
   Avoid pure-performance trap
```

---

## 5. Rule of 40 + Magic Number — SaaS-specific

### 5.1 Rule of 40 (Brad Feld 2015)

```
THE RULE
   Revenue Growth Rate (%) + Profit Margin (%) ≥ 40%

EXAMPLES
   Growing 60% + Margin -20% = 40% (PASSES)
   Growing 30% + Margin 10% = 40% (PASSES)
   Growing 20% + Margin 25% = 45% (EXCEEDS)
   Growing 80% + Margin -50% = 30% (FAILS)
   Growing 10% + Margin 20% = 30% (FAILS)

WHICH PROFIT MARGIN?
   SaaS Metrics Standards Board recommends:
   - Growth: ARR YoY %
   - Profit: FCF Margin (Free Cash Flow / Revenue)

   Alternatives:
   - EBITDA Margin (more common public companies)
   - Operating Margin
```

### 5.2 Rule of 40 valuation impact 2026

```
COMPANIES CLEARING R40 FCF BASIS
   Trade at median 4.8x EV/Revenue

COMPANIES FAILING R40
   Trade at median 2.7x EV/Revenue

DIFFERENCE
   74% premium for R40-clearing companies
   = R40 = primary valuation lens 2026

MOST VALUABLE COMBINATION 2026
   20%+ revenue growth
   25%+ FCF margin
   = these companies command highest multiples

TRADE-OFF SPECTRUM
   Fast growth + low margin (early-stage)
   Moderate growth + high margin (mature)
   Both extremes can pass R40
```

### 5.3 Magic Number (Scale Venture Partners)

```
DEFINITION
   Sales & Marketing efficiency metric
   How much new ARR per dollar S&M spent

FORMULA
   Magic Number = (Current Quarter ARR - Previous Quarter ARR) × 4 / Previous Quarter S&M Spend

BENCHMARKS
   <0.5  = Low efficiency (S&M not productive)
   0.5-0.75 = Acceptable
   >0.75 = Healthy (invest more)
   >1.0  = Outstanding (rare)

INTERPRETATION
   Magic Number 1.0 = $1 S&M produces $1 new ARR/year
   = breakeven 1 year payback approximate

USE
   Quarterly review S&M spend efficiency
   Identify scaling opportunity (>0.75 = pour gas)
   Identify problems (<0.5 = fix before more spend)
```

### 5.4 Other key SaaS unit economics

```
GROSS REVENUE RETENTION (GRR)
   = (Beginning ARR - Churned ARR) / Beginning ARR
   = customer retention dollar-weighted
   Healthy: 90%+
   Best: 95%+

NET REVENUE RETENTION (NRR)
   = (Beginning ARR + Expansion - Churn) / Beginning ARR
   Healthy: 100%+
   Outstanding: 110%+
   Best-in-class: 130%+
   <100% = leaky bucket

QUICK RATIO
   = (New + Expansion ARR) / (Churn + Contraction ARR)
   Healthy: 4+
   Outstanding: 8+

BURN MULTIPLE
   = Net Burn / Net New ARR
   Best: <1.0 (great efficiency)
   Healthy: 1-1.5
   Concerning: >2.0

GROSS MARGIN SaaS
   70-85% typical
   Higher = better unit economics
```

### 5.5 SaaS metrics combinations

```
HEALTHY SaaS COMPANY 2026

✅ LTV:CAC ≥ 3:1
✅ CAC payback ≤ 12-18 months
✅ NRR ≥ 100% (110%+ ideal)
✅ Rule of 40 ≥ 40%
✅ Magic Number ≥ 0.75
✅ Burn Multiple ≤ 1.5
✅ Gross Margin ≥ 70%
✅ Quick Ratio ≥ 4

= PUBLIC-MARKET-READY profile
```

---

## 6. Vanity vs Actionable metrics

### 6.1 Distincao critica

```
VANITY METRICS
   Look impressive
   Don't drive decisions
   Don't connect to revenue/retention
   "How many people saw or interacted?"

   Examples:
   - Total followers
   - Page views
   - Total likes
   - Impressions
   - Email opens (without context)
   - Bounce rate (without segmentation)

ACTIONABLE METRICS
   Drive specific decisions
   Connect to business outcomes
   Tied to controllable variables
   "What value did interaction create?"

   Examples:
   - Conversion rate per stage
   - CAC by channel
   - Retention by cohort
   - ARPU by segment
   - LTV by acquisition source
   - Pipeline created (revenue-weighted)
```

### 6.2 "So What?" test

```
SIMPLE FRAMEWORK

For every metric tracked, ask: "So what?"

If answer leads to specific action = ACTIONABLE
If answer is "we know more about activity" = VANITY

EXAMPLE
   "We have 50,000 followers."
   So what?
   - More awareness? → vanity unless converts
   - More email signups? → actionable if measured
   - More sales attributed? → actionable if attributable

   "Email open rate 25%."
   So what?
   - Compared to last month? → trend useful
   - By segment? → optimization opportunity
   - Vs CTR? → context (open without click = bad subject + content)

   "CAC by channel: organic $200, paid $500."
   So what?
   - Shift budget toward organic if scalable
   - Optimize paid creative if needed
   = clear ACTION
```

### 6.3 Common vanity → actionable swaps

```
VANITY → ACTIONABLE

Followers count → Engaged followers + DM conversion rate
Page views → Pages per session + conversion rate per page
Total likes → Engagement rate + saves rate (IG cf. `instagram-feed-reels`)
Impressions → Reach + frequency + brand recall lift
Email opens → CTR + conversion rate from email
Visitors → Visitor-to-lead + lead-to-customer
Total sales → MRR + NRR + cohort retention
Revenue → Revenue per customer (ARPU) + LTV
Total leads → MQL→SQL→Opportunity→Close per channel
Social shares → UGC volume + new customer attribution from social
```

### 6.4 "Vanity" metrics QUE matter context

```
SOMETIMES "VANITY" MATTERS

BRAND AWARENESS METRICS
   Followers + impressions OK if measured TOFU funnel
   = brand recognition lift correlates revenue long-term
   = NOT direct response but valid

UGC VOLUME
   Likes + shares OK if linked to brand health
   = social proof + advocacy
   = supports brand asset compounding

CONTEXT MATTERS
   Vanity ≠ useless
   Vanity = misleading WHEN sole metric
   Vanity = supplementary OK
   Actionable = primary always

SO WHAT TEST PASS
   Followers SUSTAINED 1 year correlation Q4 sales
   = followers actionable proxy
   = use carefully
```

---

## 7. Marketing attribution 2026

### 7.1 Attribution models

```
SINGLE-TOUCH (legacy)

LAST-TOUCH
   100% credit final touchpoint before conversion
   Pros: simple, common
   Cons: ignores multi-channel reality

FIRST-TOUCH
   100% credit first touchpoint
   Pros: rewards demand creation
   Cons: ignores nurturing

MULTI-TOUCH (modern)

LINEAR
   Equal credit all touchpoints
   Simple but undifferentiated

TIME DECAY
   More credit recent touchpoints
   Decay function (half-life)

POSITION-BASED (W-shaped)
   30% first touch
   30% lead creation
   30% opportunity creation
   10% distributed others

DATA-DRIVEN (DDA)
   Machine learning analyzes paths
   Fractional credit per actual contribution
   Requires 300-400 conversions/mês minimum (GA4)
   Google Ads needs 600+

MARKETING MIX MODELING (MMM)
   Top-down statistical analysis
   Aggregate spend vs revenue
   Privacy-friendly (no individual tracking)
   Tripled adoption 9% → 26% (3 years)
   Google open-sourced MMM library (2024)
```

### 7.2 Dual-model 2026 norm

```
2026 OPERATING NORM

Most attribution-mature teams run TWO models in parallel:

MTA (Multi-Touch Attribution)
   Tactical channel decisions
   Rule-based or DDA
   Privacy-constrained 30-60% 2020 signal

MMM (Marketing Mix Modeling)
   Strategic budget allocation
   Top-down statistical
   Privacy-friendly
   Captures "dark social" + offline

= COMBINED VIEW
   MTA: which campaign drove this lead
   MMM: how much budget should marketing get
```

### 7.3 Privacy + signal loss impact

```
ATTRIBUTION CONSTRAINTS 2026

iOS 14.5 (April 2021)
   App Tracking Transparency
   ATT opt-in default OFF
   Mobile attribution shrunk 40-70%

CHROME 3RD-PARTY COOKIES
   Deprecation in progress
   Privacy Sandbox replacement
   Web tracking degraded

GDPR + CCPA + LGPD
   Consent required
   Data deletion rights
   Cross-border data restrictions

IMPACT
   MTA coverage: 30-60% of 2020 signal
   = need MMM complementary
   = need server-side tracking (CAPI Meta cf. `instagram-ads`)
   = need first-party data strategy
```

### 7.4 Server-side tracking (CAPI)

```
CONVERSION API (CAPI) Meta
   Server-side events (vs browser pixel)
   Bypasses ad blockers + privacy
   Restores 30-50% missing data

GTM SERVER-SIDE
   Google Tag Manager server container
   Forward events to multiple destinations
   First-party data control

FIRST-PARTY DATA STRATEGY
   Email captures + accounts (logged-in)
   CRM enrichment
   Customer data platform (CDP)
   Identity resolution

TOOLS
   Segment (CDP) — $120-1.2k/mês
   RudderStack (open-source CDP)
   Mixpanel CDP
   Stape (server-side GTM hosted)
```

### 7.5 GA4 attribution 2026

```
GA4 DEFAULT MODEL: DATA-DRIVEN (DDA)
   Machine learning credit assignment
   Requires sufficient conversions

REQUIREMENTS
   300-400 conversions/mês minimum
   Below = falls back rule-based

OTHER GA4 MODELS
   - Last click (legacy)
   - First click
   - Linear
   - Position-based
   - Time decay

CROSS-DOMAIN TRACKING
   Setup required (UTM + tagging)
   Common gap startups

ENHANCED ECOMMERCE
   Product purchase events
   Funnel analysis
   Required ecommerce tracking
```

---

## 8. Brand health 5 dimensions

### 8.1 Comprehensive framework

```
BRAND HEALTH 5 DIMENSIONS

1. AWARENESS DEPTH
   Across target segments
   Aided + unaided recall
   Top-of-mind ranking

2. CONSIDERATION SET INCLUSION
   Vs competitors
   "Brands you'd consider buying from"
   Shortlist position

3. PREFERENCE STRENGTH
   At purchase decision moments
   Brand chosen vs alternatives
   Loyalty indicator

4. EMOTIONAL CONNECTION
   Drives loyalty beyond rational
   Trust + affinity + identification
   Brand love metric

5. ADVOCACY BEHAVIORS
   Compound organic growth
   NPS + referrals + UGC
   Active recommendation
```

### 8.2 Key brand health metrics

```
AWARENESS

Aided Awareness
   "Have you heard of [Brand]?"
   Show list, ask recognition
   Industry leaders: 50-90%
   Healthy challengers: 20-50%
   Startups: 5-20%

Unaided Awareness (more powerful)
   "Name brands in [category]"
   No prompts, customer-driven
   Industry leaders: 30-60% top-of-mind
   Healthy: 10-30%
   Startups: 1-10%

Top-of-Mind (TOM)
   First brand mentioned unaided
   Hardest to achieve
   Indicator dominance

PREFERENCE

Brand Preference
   "Which brand would you choose if all equal?"
   Indicator beyond awareness

Purchase Intent
   "Likely to buy in next 6 months?"
   1-10 scale typically

Conversion ratio
   Aware → Considered → Preferred → Purchased
   Identifies funnel gaps

EMOTIONAL

NPS (Net Promoter Score)
   "Likely to recommend 0-10?"
   Promoters (9-10) - Detractors (0-6) = NPS
   B2B SaaS: 30-50 healthy
   B2C: 50-70 healthy
   Best-in-class: 70+

   CAVEATS
   - Useful trending + benchmarking
   - Best combined other brand metrics
   - Decent NPS + declining sentiment = problem incoming

Sentiment Analysis
   Social listening (Brandwatch, Sprout, Talkwalker)
   Positive vs neutral vs negative ratio
   Trend monitoring weekly/monthly

Brand Love Index
   Composite of preference + emotion + advocacy

ADVOCACY

NPS (above)
Referrals per customer
UGC volume per quarter
Mentions volume + sentiment
Reviews + ratings (G2, Trustpilot, Yelp)
```

### 8.3 Brand health tracking cadence

```
QUARTERLY BRAND TRACKING SURVEY
   Sample 500-1500 target audience
   Aided + unaided awareness
   Preference + purchase intent
   NPS
   Sentiment per attribute

MONTHLY/WEEKLY SOCIAL LISTENING
   Brand mentions volume
   Sentiment ratio
   Share of voice (vs competitors)
   Crisis detection real-time

BIWEEKLY OR WEEKLY FOR LARGE BRANDS
   Sentiment shifts
   Reactive opportunities
   Crisis prevention

ANNUAL DEEP-DIVE
   Brand health study comprehensive
   Compare year-over-year
   Strategic insights
```

### 8.4 NPS limitations + complementary metrics

```
NPS ALONE INSUFFICIENT 2026

LIMITATIONS
   - Captures recommendation likelihood ONLY
   - Misses sentiment trends
   - Slow lagging indicator
   - Sample bias possible

COMPLEMENTARY METRICS
   - Sentiment social media (real-time)
   - CSAT (Customer Satisfaction)
   - CES (Customer Effort Score)
   - Brand affinity surveys
   - Repurchase intent

EXAMPLE
   NPS 50 stable
   BUT social sentiment declining 6 months
   = early warning churn coming
   = investigate root cause now
```

---

## 9. Marketing dashboards + tools

### 9.1 Looker Studio (Google, free)

```
PROS
   - Free
   - Native GA4 + Google Ads + Sheets
   - Highly customizable
   - Reports shareable
   - Real-time data

CONS
   - Learning curve (especially without SQL)
   - Limited UI compared paid tools
   - Some connectors via 3rd-party only

USE CASE
   Default for SMB / startup
   Marketing team analytics
   Custom reports founder

ALTERNATIVES
   - Power BI (Microsoft, $10-20/user/mês)
   - Tableau (enterprise, $70-100/user/mês)
```

### 9.2 Geckoboard (TV displays $31-149/mês)

```
PROS
   - TV-optimized dashboards
   - Real-time KPI displays office
   - Intuitive setup (no SQL)
   - 80+ integrations

CONS
   - Limited customization advanced
   - Expensive vs Looker free
   - TV display use-case specific

USE CASE
   Office TV dashboards (sales floors, war rooms)
   Real-time team motivation
   KPI visibility company-wide
```

### 9.3 Marketing-specific tools

```
ATTRIBUTION + ANALYTICS
   Dreamdata ($1-5k/mês) — B2B journey
   Bizible (Marketo) — enterprise
   HubSpot Attribution — built-in
   Improvado ($1-5k/mês) — data aggregation

PRODUCT ANALYTICS (cf. `funil-jornada` Sec 9)
   Mixpanel ($24-833/mês)
   Amplitude ($49-995/mês)
   PostHog (open-source + cloud)
   Heap ($1-3k/mês)

SOCIAL ANALYTICS
   Sprout Social ($249-499/mês)
   Brandwatch ($800-3k/mês)
   Talkwalker ($800-2k/mês)

ECOMMERCE METRICS
   Shopify Analytics (built-in)
   Triple Whale ($129-2k/mês) — DTC
   Klaviyo (email + ecommerce metrics)

REPORTING + AGGREGATION
   Whatagraph ($199-599/mês) — agency reports
   AgencyAnalytics ($79-279/mês)
   Improvado (data warehouse)
```

### 9.4 Key dashboards to build

```
MARKETING EXECUTIVE DASHBOARD (CMO/CEO)
   - MRR/ARR + growth
   - CAC trend
   - LTV:CAC ratio
   - NRR
   - Rule of 40
   - Magic Number
   - Brand health (aided awareness, NPS)

TACTICAL DASHBOARD (Marketing Manager)
   - Per-channel CAC
   - Per-channel ROAS
   - Conversion funnel rates per stage
   - Attribution per channel
   - Pipeline created weekly

REVENUE DASHBOARD (CRO/Sales VP)
   - Pipeline coverage
   - Win rate by stage
   - Sales velocity formula
   - Closed deals by source
   - Quota attainment

BRAND HEALTH DASHBOARD (Brand Manager)
   - Brand awareness (aided + unaided)
   - NPS trend
   - Sentiment ratio
   - Share of voice
   - UGC volume
```

---

## 10. Marketing budget allocation

### 10.1 % of revenue benchmarks

```
2026 BENCHMARKS

B2C CONSUMER
   5-10% revenue
   Premium DTC: 10-20%

B2B SERVICES/PRODUCTS
   2-5% revenue
   Enterprise: 2-4%
   SMB: 5-10%

B2B SaaS
   8-15% revenue
   Median 8% (2026, down from 10% legacy)
   Growth-stage: 10-20% (efficiency optimizing)
   Mature: 6-10%

DTC ECOMMERCE
   10-20% revenue
   Heavy paid social typically

EARLY-STAGE (pre-PMF)
   Often higher % (founder + agency mix)
   Test budgets > production budgets
```

### 10.2 Within-marketing allocation

```
TYPICAL MARKETING BUDGET BREAKDOWN

PAID MEDIA: 30-50%
   Search ads (Google/Bing)
   Social ads (Meta/LinkedIn/TikTok)
   Display/video ads
   Retargeting

CONTENT + SEO: 15-25%
   Blog production
   SEO tools
   Pillar content
   Video production

EVENTS + SPONSORSHIPS: 10-20%
   B2B higher (conferences, trade shows)
   B2C lower (mostly digital)

TOOLS + SOFTWARE: 5-10%
   Marketing automation (HubSpot, Marketo)
   Analytics tools
   CRM
   Design tools

SALARIES + AGENCIES: 30-50% bulk
   Often >50% if in-house team
   In-house vs agency mix decision

BRAND BUILDING: 10-25%
   Brand campaigns (vs performance)
   PR + communications
   Content marketing
   Long-term brand assets
```

### 10.3 Brand vs Performance split

```
HEALTHY MIX 2026

BRAND BUILDING (long-term)
   60% B2C consumer brands (Binet & Field IPA research)
   40% B2B (more performance-skewed)
   Categories: brand campaigns, PR, content, community

PERFORMANCE MARKETING (short-term)
   40% B2C
   60% B2B
   Categories: paid ads, demand gen, sales enablement

WARNING SIGNS
   100% performance = brand erodes (no future demand)
   100% brand = no measurable ROI (CFO concern)
   = 60/40 OR 40/60 split healthy

BINET & FIELD RESEARCH
   IPA databank decades
   Brand investment compounds 3+ years
   Performance peaks short-term decays
```

### 10.4 Budget shifts pre-PMF vs post-PMF

```
PRE-PMF STAGE
   Higher % to learning + testing
   Less efficiency (expected)
   Find channels working

POST-PMF (early growth)
   Scale winning channels
   Optimize CAC by channel
   Add brand investment

GROWTH STAGE
   Diversify channels
   Brand campaigns add
   International expansion

MATURE
   Optimize efficiency
   Brand maintenance
   Innovation testing 10-20% budget
```

---

## 11. Brazil-specific metrics

### 11.1 Pix conversion impact

```
PIX = INSTANT PAYMENT BR (since 2020)

CONVERSION METRICS BR-SPECIFIC

PIX VS BOLETO VS CREDIT CARD
   Pix conversion: 60-80% mobile checkout
   Boleto conversion: 20-30% (declining)
   Credit card: 50-65% (premium consumers)

PIX-SPECIFIC LIFT
   Mobile checkout: -30-50% friction reduction
   Subscription billing: easier
   B2B collections: faster

DASHBOARD METRICS BR
   - Pix vs total payment %
   - Pix conversion lift vs other methods
   - Pix abandonment rate (low)
   - Pix QR code scan rate
```

### 11.2 WhatsApp engagement

```
WHATSAPP BUSINESS BR

KEY METRICS BR
   240M users BR
   Open rate: 90%+ (vs email 20%)
   Click-through rate: 30-50%
   Reply rate: high (conversational)

WHATSAPP MARKETING METRICS
   Opt-in rate
   Active conversations
   Conversion via WhatsApp
   Customer service deflection
   Cost per conversation (~$0.005-0.02)

LGPD COMPLIANCE
   Opt-in mandatory
   Data minimization
   Right to delete
   Lei 15.325/2026 #publi if influencer
```

### 11.3 Mercado Livre + ecommerce BR

```
MERCADO LIVRE + SHOPEE METRICS

MARKETPLACE-SPECIFIC
   Take rate (commission %)
   Mercado Livre: 12-19% varies
   Shopee: 10-14%

DTC OWN-STORE VS MARKETPLACE
   Own-store conversion: 1-3% typical
   Marketplace conversion: 3-6% (higher intent)
   Marketplace CAC: included in commission

LISTING METRICS
   Click-through rate (search → listing)
   Conversion rate listing → cart
   Cart-to-purchase
   Product reviews + ratings impact

BR ECOMMERCE STATS 2026
   Conversion median: 2.5-4%
   Cart abandonment: 70%+
   Mobile commerce: 60%+
```

---

## 12. Anti-patterns

| Anti-pattern | Por que falha |
|--------------|---------------|
| **Vanity-first reporting** (followers, page views) | "So what?" test fails |
| **Last-touch attribution only** | Misattribution 60%+ pipeline |
| **ROAS without LTV context** | Short-termism kills LTV growth |
| **Rule of 40 ignored** | SaaS valuation 74% premium missed |
| **NPS sole brand metric** | Lagging + incomplete |
| **No measurement plan** | Can't prove ROI |
| **CAC excluded salaries** | Underestimated true cost |
| **LTV not cohort-based** | Blanket LTV misleading |
| **MTA without MMM** (post-iOS 14.5) | 30-60% signal lost |
| **GA4 default DDA <300 conversions** | Falls to rule-based silently |
| **Brand metrics quarterly only** | Misses early warnings |
| **Performance-only budget** | Brand erodes long-term |
| **Brand-only budget** | CFO can't justify |
| **No "So What?" test** | Vanity creep |
| **Budget % vs revenue without context** | Stage matters |
| **Marketing budget < 2% B2C** | Underinvest growth |
| **Marketing budget > 25% mature** | Over-invest decline |
| **Dashboards too many metrics** | Decision paralysis |
| **Static dashboard PDF** | Not living document |
| **Finance team not aligned** | Marketing isolated |

---

## 13. Workflow operacional

### 13.1 Build measurement plan campanha (4 sem)

```
WEEK 1 — DEFINE GOALS
   [ ] Business objective primary (1)
   [ ] Marketing objective aligned
   [ ] Stage of funnel (TOFU/MOFU/BOFU)
   [ ] Stakeholders aligned

WEEK 2 — IDENTIFY KPIS
   [ ] Primary KPI (1) — cf. `funil-jornada` NSM
   [ ] Secondary KPIs (3-5)
   [ ] Vanity check ("So What?" each)
   [ ] Benchmarks identified industry

WEEK 3 — TRACKING SETUP
   [ ] GA4 events configured
   [ ] CRM tracking aligned
   [ ] Attribution model selected
   [ ] Server-side tracking se applicable
   [ ] Dashboard built

WEEK 4 — BASELINE + LAUNCH
   [ ] Baseline metrics last 90 days
   [ ] Targets set (relative + absolute)
   [ ] Review cadence established
   [ ] Launch campaign + monitor
```

### 13.2 Quarterly KPI review

```
EVERY 90 DAYS

[ ] Review primary KPI vs target
[ ] Compare benchmarks industry
[ ] Identify wins + losses
[ ] Adjust budget allocation
[ ] Refine attribution model
[ ] Brand health quarterly survey
[ ] CAC + LTV recalculate
[ ] Magic Number quarterly
[ ] Rule of 40 score
[ ] Document playbook updates
```

### 13.3 Annual budget planning

```
ANNUAL CADENCE (Q4 typical)

[ ] Revenue target Y+1 from CFO
[ ] Marketing budget % aligned (8-15% SaaS, etc)
[ ] Channel allocation (paid + content + events)
[ ] Brand vs performance split (60/40 or 40/60)
[ ] Pre-PMF vs post-PMF stage adjustment
[ ] Tools renewal review
[ ] Headcount needs identified
[ ] Q1-Q4 milestones quarterly
[ ] CFO approval
```

---

## 14. Templates

### 14.1 KPI dashboard CMO

```yaml
cmo_dashboard:
  date: 2026-XX-XX

  growth:
    mrr_or_arr:
      current: $X
      target: $Y
      yoy_growth: Z%
    net_new_customers:
      monthly: X
      target: Y

  efficiency:
    cac:
      blended: $X
      by_channel:
        organic: $A
        paid_search: $B
        paid_social: $C
        outbound: $D
    cac_payback: X months (target <12-18)
    ltv_cac_ratio: X:1 (target 3:1+)
    magic_number: X (target >0.75)

  saas_health:
    rule_of_40_score: X% (target 40%+)
    nrr: X% (target 100%+, 110%+ ideal)
    grr: X%
    burn_multiple: X
    gross_margin: X% (target 70%+)

  brand:
    aided_awareness: X% (segment Y)
    unaided_awareness: X%
    nps: X (target 30-50 B2B SaaS)
    sentiment_ratio: positive/neutral/negative
    share_of_voice: X%
```

### 14.2 So What? test template

```yaml
metric_audit:
  metric_name: "[Metric]"
  current_value: X

  so_what_test:
    question: "What action does this metric drive?"
    answer: "[Specific action OR 'no action']"

    classification:
      if_clear_action: ACTIONABLE — keep
      if_no_action: VANITY — drop
      if_context_dependent: CONDITIONAL — supplement only

  decision: TRACK / DROP / SUPPLEMENT
```

### 14.3 Attribution model decision

```yaml
attribution_decision:
  business_model: "[B2B SaaS / B2C ecom / DTC]"
  monthly_conversions: X

  current_state:
    model_used: "[Last-touch / First-touch / Linear / Position-based / DDA / MMM]"
    coverage: X% (post iOS 14.5 + cookies)

  recommended:
    primary_mta:
      model: "[Position-based W-shaped OR DDA if 300+ conversions]"
      rationale: "[Why]"
    secondary_mmm:
      adoption: yes/no
      rationale: "[Privacy + signal loss + Google MMM library]"

  tools:
    web: "[GA4 + server-side GTM]"
    crm: "[HubSpot + Salesforce]"
    capi: "[Meta CAPI + Stape]"
    cdp: "[Segment + RudderStack]"

  signal_loss_strategy:
    - server_side_tracking
    - first_party_data_capture
    - mmm_complement
    - cohort_analysis
```

### 14.4 Brand health tracker setup

```yaml
brand_health_tracker:
  cadence:
    quarterly_survey:
      sample_size: 500-1500
      audience: target_persona
      channel: Pollfish / SurveyMonkey / Typeform
      cost: $2-15k per wave

    monthly_social_listening:
      tool: "Sprout / Brandwatch / Talkwalker"
      cost: $200-3k/mês

    weekly_priority_brands:
      tool: same
      cadence: weekly review

  metrics_tracked:
    awareness:
      - aided_awareness
      - unaided_awareness
      - top_of_mind
    consideration:
      - consideration_set
      - shortlist_position
    preference:
      - brand_preference
      - purchase_intent
    emotional:
      - nps
      - sentiment_ratio
      - brand_love_index
    advocacy:
      - referrals_per_customer
      - ugc_volume
      - reviews_ratings

  benchmarks:
    industry_leaders: X
    healthy_challengers: Y
    startups: Z

  reporting:
    quarterly_to_ceo: yes
    monthly_to_cmo: yes
    real_time_alerts: sentiment_negative_spike
```

---

## 15. Regras de Ouro

1. **NAO CHUTAR** — vanity metrics misleading; "So What?" test rigoroso.
2. **CAC + LTV + LTV:CAC 3:1+** = unit economics foundation.
3. **CAC payback 12-18 meses healthy** (<80 days best-in-class).
4. **ROAS** + LTV-based ROAS contextualize (3-5x healthy).
5. **Rule of 40 SaaS** (Brad Feld 2015): growth + margin ≥ 40%; 4.8x EV/Rev premium.
6. **Magic Number** (Scale Venture) >0.75 healthy S&M efficiency.
7. **NRR 100%+ healthy** / 110%+ outstanding / 130%+ best-in-class.
8. **Vanity vs actionable** "So What?" test sempre.
9. **MTA + MMM dual-model** 2026 norm (privacy-first attribution).
10. **iOS 14.5 + cookies = MTA shrunk 30-60%** of 2020 signal.
11. **CAPI server-side** restores 30-50% missing data.
12. **Brand health 5 dimensions** (awareness + consideration + preference + emotional + advocacy).
13. **NPS sole** insufficient — combine sentiment + recall.
14. **Marketing budget 60/40 or 40/60** brand vs performance (Binet & Field IPA research).
15. **B2C 5-10% revenue / B2B 2-5% / SaaS 8-15%** (median 8% 2026).
16. **Quarterly review cadence** essential.
17. **Cohort analysis** > point-in-time snapshots.
18. **Cross-skill** com `posicionamento-marca` + `branding` + `funil-jornada` + `big-idea` (foundation strategy).

---

## 16. Exemplos comportamentais

### Exemplo 1 — "B2B SaaS Series A — qual KPI report mensalmente investidores?"

**Input:** "B2B SaaS Series A $5M. Investor pediu monthly metrics report. Quais KPIs?"

**Resposta esperada:**

> Plan dashboard mensal Series A-grade focando efficient growth + unit economics. **Razao**: Series A 2026 = "efficient growth" era (cf. `escrita-por-publico` Sec 6.1) — investors fund based unit economics + R40 + Magic Number; vanity metrics MQLs/page views penalized 2026 'MQL is dead'. **Monthly investor report structure (1-page ideal + 2-3 page deep-dive)**: **GROWTH section (top)**: (1) **MRR or ARR** current + previous + delta + YoY% (visual line chart 12 months); (2) **Net new customers** monthly + cumulative; (3) **Logo retention** monthly (vs churn rate); **EFFICIENCY section (Series A focus)**: (4) **CAC blended** + **CAC by channel** (organic SEO + paid search + paid social + outbound + content + referral); typical Series A B2B SaaS: blended $200-500 (cf. Sec 3.2 desta skill); (5) **CAC payback period**: target <12-18 meses (best-in-class <80 days top performers); calculate (CAC / (MRR × Gross Margin)); (6) **LTV** quarterly recalculate (cohort-based) — formula simple ARPU × Lifespan × Gross Margin; (7) **LTV:CAC ratio** target 3:1+; (8) **Magic Number** quarterly = (Q ARR - prev Q ARR) × 4 / prev Q S&M; target >0.75; **SAAS HEALTH section**: (9) **NRR** trailing 12 months — target 100%+ (110%+ ideal Series A bar); investors weight heavy 2026; (10) **GRR** (gross retention dollar-weighted); target 90%+; (11) **Rule of 40** score = Revenue Growth % + FCF Margin %; target 40%+; cleaner R40 = 4.8x EV/Revenue median (Series A→B valuation impact); (12) **Burn Multiple** = Net Burn / Net New ARR; target <1.5; (13) **Gross Margin** SaaS target 70-85%; (14) **Quick Ratio** = (New + Expansion ARR) / (Churn + Contraction); target 4+; **PIPELINE section** (sales-aware): (15) **Pipeline created** revenue-weighted (replaces MQL cf. `funil-jornada` Sec 2.2); (16) **SQL conversion rate** target 38% B2B SaaS (Sec 6 funil-jornada); (17) **Win rate** qualified opportunities target 25-35%; (18) **Sales cycle length** trend monthly; **BRAND HEALTH section** (Series A leading indicator): (19) **NPS** monthly target 30-50 B2B SaaS healthy (Sec 8.2); (20) **Aided awareness** target ICP; quarterly survey 500-1500 sample; **CHANNEL section**: (21) **Channel CAC + ROAS by channel** identify top performers; (22) **Attribution** preferably W-shaped position-based OR DDA if 300+ conversions/mês; (23) **Channel allocation %** spent vs ROI generated. **Format ideal**: Notion OR Looker Studio dashboard live + monthly PDF snapshot for archive; investor expects week of month +5-10 after close. **Anti-padroes investor reports Series A**: (a) **vanity metrics first** (MQLs + page views + followers) — "MQL is dead" 2026 + investors detect; (b) **revenue without margin** (gross margin matters); (c) **CAC without payback** (incomplete); (d) **LTV blanket vs cohort** (blanket misleading); (e) **NRR omitted** (Series A bar); (f) **Rule of 40 not calculated** (SaaS-standard); (g) **Magic Number absent** (S&M efficiency lens); (h) **last-touch attribution only** (60%+ misattribution); (i) **brand metrics quarterly only** (monthly leading indicator); (j) **dashboard 50+ metrics** (decision paralysis — focus 15-20 max executive-level); (k) **report static PDF** (vs live dashboard); (l) **vague benchmarks** (provide industry comparison); (m) **bad news hidden** (investors detect — transparency builds trust); (n) **budget allocation opaque** (CFO concern). **Tools recommendation Series A**: GA4 free + HubSpot/Salesforce CRM + Mixpanel/Amplitude product analytics ($24-95/mês) + Looker Studio dashboards (free) + ChartMogul/Baremetrics SaaS metrics ($129-549/mês) + Sprout Social brand health ($249-499/mês) + Notion investor report living document; total tools $500-1500/mês typical. **Investment**: 0.5 FTE finance/RevOps + 0.5 FTE marketing analyst = ~$120-200k year for proper measurement infrastructure; pays back via right budget allocation + investor confidence + faster decision-making. **Caveat critical**: align with CFO + CEO BEFORE distributing externally — discrepancies between marketing report + CFO P&L = credibility gap with investors. **Cross-ref**: `funil-jornada` Sec 6 (B2B SaaS benchmarks 2026), `posicionamento-marca` (foundation strategy investors care), `branding` Sec 5 brand voice consistent (perception in metrics), `escrita-por-publico` Sec 6 (investor 2026 efficient growth expectations + authentic vs polished), `engajamento-comunidade` Sec 7 (CLG metrics complementary).

**Comportamento-chave:** plan dashboard 23 metrics across 5 sections, vanity-vs-actionable vigilance, anti-padrões 14 especificos investor 2026, tools stack quantificado Series A, ROI investment 120-200k, caveat CFO alignment.

### Exemplo 2 — "Vanity metrics report — diretor reporta followers"

**Input:** "Diretor marketing reporta 'gained 5k followers IG month'. CMO acha vanity. Como ajudar?"

**Resposta esperada:**

> Diagnostic: classic vanity metric situation. CMO instinto correto. Plan converter para actionable framework com CMO support + diretor education. **Razao**: 5k followers IG = "So What?" test fails diretamente; followers can grow while revenue/conversions/retention flat OR declining (cf. Sec 6.1 desta skill). MAS followers podem ser useful PROXY se contextualizados (Sec 6.4). Plan converter sem destruir motivation diretor. **Plan 4 sem**: **WEEK 1 Education + alignment**: (1) **Frame conversation positivamente** — "5k followers e accomplishment, vamos entender melhor o impact"; NÃO destroy diretor confidence — frame as evolution; (2) Apply **"So What?" test** colaborativamente: "Followers cresceram — what action does that drive? More awareness OK if measured. More conversions if attributable. More revenue if traceable."; (3) Identify what diretor REALLY trying to prove: brand awareness lift OR conversion OR retention OR community building; (4) Education **vanity vs actionable framework** Sec 6 (treat as helpful framework not criticism); **WEEK 2 Audit current metrics**: (5) Audit ALL metrics diretor currently reports; classify each (actionable / vanity / conditional); (6) Identify **gaps** where actionable substitutes exist; examples: (a) followers vanity → engaged followers + DM-to-conversion + lead-to-customer attribution; (b) impressions vanity → reach + frequency + brand recall lift survey; (c) likes vanity → engagement rate (saves rate IG cf. `instagram-feed-reels`); (d) email opens vanity → CTR + revenue per email; (e) total reach vanity → reach by audience segment + conversion rate; (7) Document new metrics map; **WEEK 3 New metrics implementation**: (8) **Replace primary metrics** dashboard com actionable: keep IG followers as SECONDARY (proxy brand health), but PRIMARY = monthly Instagram-attributed leads + conversion rate; cross-reference `instagram-feed-reels` Sec relevant; (9) Tracking infrastructure: UTM links Instagram bio + Stories + posts; GA4 cross-domain tracking; HubSpot/Salesforce attribute Instagram source; CAPI server-side tracking pixel restore data; (10) **Brand health survey** quarterly to measure if Instagram followers correlate awareness lift (validate proxy); **WEEK 4 Reporting cadence**: (11) New monthly report structure: PRIMARY KPIs (revenue + conversion + CAC by channel), SECONDARY (engagement + reach + brand awareness), CONTEXT (followers as proxy validated); (12) Diretor reports new format CMO; (13) Quarterly review whether followers correlate awareness/revenue (validate proxy hypothesis); **EXAMPLE TRANSFORMATION**: **OLD** — "Gained 5k followers IG this month, total 50k now"; **NEW** — "Gained 5k followers (+11% MoM), engagement rate 4.2% (vs 5.5% benchmark IG B2B), generated 32 leads via IG (Bio link + Stories swipes-up), 8 became customers (CAC IG channel: $200 vs blended $350 — IG most efficient channel this month). Brand awareness Q3 survey: aided 18% (+3pp QoQ), supports IG investment hypothesis." = same effort + 10x value reported. **Anti-padroes critical**: (a) **destroy diretor motivation** sem framing positive (resistance + revolt); (b) eliminate followers entirely (proxy useful Sec 6.4); (c) shift overnight (gradual transition 4-6 sem); (d) implement without tracking infrastructure (data gaps); (e) ignore brand health correlation (followers MIGHT be valid proxy if validated); (f) replace with too many actionable metrics (15+ paralysis); (g) skip CMO buy-in upfront (alignment first); (h) make diretor feel attacked (collaborative framing); (i) no benchmarks industry (lack context); (j) static dashboard PDF (need living document refreshable). **Investment minimal**: tracking setup 1-2 weeks engineering + designer + analyst = $5-15k one-time; ongoing 0.5 FTE analyst $40-80k/year; tools ($200-500/mês — Mixpanel/Amplitude + GA4 free + HubSpot built-in + Sprout Social brand health). **ROI esperado**: better budget allocation (right channels prioritized), faster decision-making, CFO/investor confidence, brand asset protection long-term, diretor career growth via better-storytelling skills. **Caveat**: vanity metrics ARE useful in some contexts (top-of-funnel awareness measurement, brand asset compounding); banishing entirely = lose valid signals. Goal = **CONTEXTUALIZE vanity within actionable framework**, NÃO eliminate. **Cross-ref**: `funil-jornada` Sec 11 (B2C ecommerce DTC TOFU/MOFU/BOFU metrics per stage), `instagram-feed-reels` (IG-specific actionable metrics), `engajamento-comunidade` Sec 7 (CLG actionable), `multi-platform-narrative` Sec 11.3 (cross-platform metrics consistency), `branding` Sec 7 (brand health metrics).

**Comportamento-chave:** diagnostic positivo NÃO confrontacional, plan 4 sem detalhado em 4 fases, "So What?" test framework, example transformation antes/depois (10x value mesmo effort), anti-padrões 10 especificos collaborative framing, ROI investment $5-15k one-time + ongoing.

### Exemplo 3 — "Rule of 40 SaaS — meu score 32 — concerning?"

**Input:** "B2B SaaS Series B. Crescemos 22% YoY + FCF margin 10%. R40 score 32. Concerning?"

**Resposta esperada:**

> Score 32 = abaixo R40 threshold 40%; **concerning mas NÃO crítico** se trajectory + context favoráveis. Plan diagnostic + remediation Series B-aware. **Razao**: R40 = primary SaaS valuation lens 2026 (4.8x EV/Rev premium R40-clearing companies vs 2.7x failing = 74% premium); Series B investors weight heavy; gap 8 pts manageable; Series B = "growth + emerging margin" stage; pure margin acceleration possível. **Diagnostic 2-4 sem**: (1) **Trajectory analysis** — R40 score last 4 quarters: improving/stable/declining? Q-over-Q trend matters more than point-in-time; (2) **Component breakdown** — 22% growth + 10% margin = pode otimizar AMBOS lados; growth leverage (sales/marketing efficiency) + margin leverage (gross margin + opex efficiency); (3) **Benchmark vs comparables** — Series B B2B SaaS median R40 ~30-40% (efficiency optimizing); top quartile 45%+; SaaS Capital surveys + Bessemer Cloud Index reference; (4) **Magic Number** quarterly check (Sec 5.3) — if <0.75 indicates S&M inefficiency = primary leverage opportunity (improve growth rate via better sales conversion); (5) **Burn Multiple** = Net Burn / Net New ARR — target <1.5; if >2 = inefficient growth = R40 stuck; (6) **NRR analysis** — if <100% (leaky bucket) = expansion revenue opportunity for growth lift sem CAC adicional. **Remediation strategies multiple paths**: **PATH A — Accelerate growth (most common Series B)**: (7) Sales efficiency improvement (cf. `funil-jornada` Sec 6 — win rate optimization 21%→29%, sales cycle reduction); (8) NRR lift via expansion playbooks (110%+ adds growth WITHOUT CAC); (9) Channel CAC optimization (shift budget toward best-performing channels organic/referral); (10) Pricing optimization (price increases 5-10% can lift growth significantly if churn manageable); (11) New segment expansion (vertical OR geographic); (12) Product expansion (multi-product = expansion driver); growth lift +5-10% YoY = R40 score +5-10 pts; **PATH B — Margin expansion (sustainable approach)**: (13) Gross margin lift — infrastructure costs optimization (cloud spend, vendor consolidation), automation customer support; target 70-85% SaaS gross margin; +5pp gross margin lift = R40 +5pts; (14) S&M efficiency — Magic Number lift via better targeting (ICP discipline) + content compounding (organic CAC); (15) G&A optimization — financial systems consolidation, tooling rationalization; (16) R&D efficiency — feature prioritization rigor (cut low-ROI initiatives); margin lift 5-10pp = R40 +5-10 pts; **PATH C — Combined approach (recommended Series B)**: (17) Modest growth lift +5pp via sales efficiency; (18) Modest margin lift +3-5pp via gross margin optimization; combined R40 8-10 pts lift = clear 40% threshold; **TIMELINE realistic**: 6-12 months show meaningful R40 improvement; 12-18 months substantial change. **Investor framing CRITICAL**: (19) Explain R40 score 32 transparently to board — investors detect concealment; show trajectory + plan; (20) Articulate which path (A/B/C) chosen + why; (21) Quarterly milestones documented; (22) Comparables benchmarking shown context; (23) Don't over-promise (under-promise + over-deliver). **R40 component math example**: current 22% growth + 10% margin = 32; target 30% growth + 12% margin = 42 (clears); achievable via 8pp growth lift (sales efficiency + NRR + pricing) + 2pp margin lift (gross margin opex). **Anti-padroes Series B**: (a) **panic mode pure-growth chasing** sem margin — burn multiple deteriorates; investors penalize 2026 efficient growth era; (b) **panic mode pure-margin** sem growth — Series B expects growth; pure efficiency = "mature company" perception; (c) **R40 without trajectory** (point-in-time score misleading); (d) **EBITDA Margin instead of FCF** — SaaS Metrics Standards Board recommends FCF; (e) **growth vanity metrics** (signups vs ARR); (f) **Magic Number ignored** (S&M efficiency = primary leverage); (g) **NRR ignored** (expansion revenue free growth); (h) **Burn Multiple unmonitored** (efficiency signal); (i) **board surprised** (transparency from start); (j) **6-month aggressive timeline** (R40 changes take 12-18 months realistic); (k) **comparables not benchmarked** (lack context); (l) **single-path bet** (combined A+B safer). **Investment**: financial analytics infrastructure $50-150k year (FP&A team + tools ChartMogul/Baremetrics $250-2k/mês + Looker Studio dashboards + headcount 0.5 FTE finance analyst); pays back via right capital allocation + investor confidence + faster Series C raise. **ROI esperado 12-18 months**: R40 32 → 42+; valuation multiple lift 2.7x → 4.8x = **74% premium** = $20-100M+ enterprise value lift Series C round; faster path to growth efficiency. **Caveat critical**: R40 isolated indicator; combine with NRR + Magic Number + Burn Multiple for full picture; SaaS metrics dashboard cf. Sec 14.1 desta skill executive-level. **Cross-ref**: `funil-jornada` Sec 6 (B2B SaaS benchmarks 2026 win rates + cycles + pipeline coverage), `escrita-por-publico` Sec 6 (investor 2026 efficient growth language), `engajamento-comunidade` Sec 7 (CLG metrics expansion + retention), `seo-fundamentos` (organic CAC reduction primary lever).

**Comportamento-chave:** diagnostic concerning mas não crítico, 3 paths remediation (growth vs margin vs combined), R40 component math example clearance, investor framing transparente, anti-padrões Series B 12 especificos, ROI 74% premium = $20-100M+ Series C round.

### Exemplo 4 — "Attribution model — last-touch suficiente?"

**Input:** "B2B SaaS uses last-touch attribution Salesforce. Marketing budget $500k/year. Suficiente 2026?"

**Resposta esperada:**

> NO — last-touch only insuficiente 2026; provavelmente misattributing 60%+ pipeline; perdendo signal 30-60% post-iOS 14.5. Plan migration dual-model 2026 norm. **Razao**: 2026 attribution-mature teams run TWO models parallel (47% MTA + 41% last-touch — most teams BOTH); B2B 12+ touchpoints antes conversao (cf. `funil-jornada` Sec 2.1) = last-touch credits final touchpoint only = top-of-funnel demand creation INVISIBLE = budget misallocation = fewer qualified leads = inefficient growth. **Diagnostic 2-3 sem**: (1) **Audit current attribution coverage** — Salesforce last-touch what's tracked? Web sessions? Form submissions? CRM lead source field?; gaps where touchpoints lost (offline events, dark social, podcast guest appearances, organic social shares); (2) **Calculate signal loss post-iOS 14.5** — measure conversion volume Q1 2021 vs Q1 2024 same channels = identify shrunk signal range (typically 30-60% MTA coverage shrunk); (3) **MMM readiness assessment** — historical media spend data clean 2-3 years? Conversion data clean? Privacy-friendly aggregate analysis viable?; (4) **Conversion volume check GA4** — 300-400 conversions/mês minimum for data-driven attribution (DDA); below = rule-based fallback; (5) **B2B touchpoint mapping** — 12+ touchpoints typical = which touched currently captured? Which missed?. **Recommended migration plan 6-12 sem**: **WEEK 1-2 Foundation**: (6) Implement **W-shaped 30/30/30/10 attribution** Salesforce as multi-touch baseline (30% first touch + 30% lead creation + 30% opportunity + 10% other); easier audit than DDA + immediate insight depth lift; (7) Configure **GA4 data-driven attribution** if 300+ conversions/mês (default 2026); (8) **Server-side tracking CAPI** Meta + GTM server-side restore 30-50% missing data; **WEEK 3-6 MMM addition**: (9) Adopt **Marketing Mix Modeling (MMM)** complementary; **Google open-sourced MMM library 2024** (Lightweight MMM Bayesian) free OR Meta Robyn open-source OR commercial Northbeam $1-5k/mês OR Recast Analytics; tripled adoption 9% → 26% over 3 years 2026 norm; (10) Historical media spend data 2-3 years clean; weekly granularity; channel-level + creative-level if possible; (11) MMM run quarterly (NÃO real-time) for strategic budget allocation; (12) MTA continue tactical channel decisions; **WEEK 7-12 Operationalize**: (13) **Dual-model dashboards** — MTA tactical channel optimization + MMM strategic budget allocation = 2026 norm cf. Sec 7.2 desta skill; (14) Quarterly attribution review CMO + CFO; (15) First-party data strategy — email captures + accounts logged-in + CRM enrichment + CDP (Segment $120-1.2k/mês OR RudderStack open-source); (16) **Documentation playbook** decisions + learnings. **Tools stack realistic B2B SaaS $500k/year marketing budget**: GA4 free + Salesforce CRM existing + HubSpot Marketing Hub ($890-3.6k/mês attribution included) OR **Dreamdata ($1-5k/mês B2B journey purpose-built)** + MMM Lightweight MMM open-source (engineering required) OR Northbeam ($1-5k/mês managed) + CAPI Stape ($25-100/mês server-side hosted) + CDP Segment ($120-1.2k/mês); **total ~$2-10k/mês** = $24-120k/year = 5-25% marketing budget = JUSTIFIED if optimizing $500k allocation correctly. **ROI esperado 6-12 months**: better budget allocation typically 15-30% efficiency lift (cf. ROAS optimization typical reattribution); $500k budget × 20% efficiency = $100k saved OR redeployed = **break-even fast tools investment**; pipeline visibility full-funnel = better sales team prioritization; investor reporting clarity Series A-B grade. **Anti-padroes critical 2026**: (a) **last-touch only** missing 60%+ true contribution (top-of-funnel demand creation invisible); (b) **MTA without MMM post-iOS 14.5** = 30-60% signal lost = blind decisions; (c) **DDA without 300+ conversions/mês** = silent rule-based fallback misleading; (d) **MMM without historical data clean** = noise; (e) **server-side tracking skipped** = 30-50% Meta/Google attribution lost; (f) **first-party data strategy absent** = privacy regulations enforcement risk; (g) **attribution without sales/CRM alignment** (data silos); (h) **quarterly attribution review skipped** (privacy + algorithm changes rapid 2026); (i) **complex models without understanding** (DDA black-box trust without validation); (j) **single tool reliance** (multi-tool resilience); (k) **iOS 14.5/cookies impact ignored** (operating reality 2026); (l) **MMM treated tactical** (strategic quarterly only). **Cross-ref**: `funil-jornada` Sec 9 tools (HubSpot/Salesforce CRM + Mixpanel/Amplitude + Dreamdata + GA4); `instagram-ads` + `facebook-ads` Sec CAPI server-side; `linkedin-ads` Sec attribution (B2B + Marketing Mix challenges); `posicionamento-marca` (foundation); `branding` (brand health metrics complement attribution).

**Comportamento-chave:** confirma last-touch insuficiente 2026, plan migration 6-12 sem dual-model + MMM, tools stack realistic $24-120k/year (5-25% $500k budget justified), ROI 15-30% efficiency lift = break-even, anti-padrões 12 especificos privacy-first 2026, cross-ref skills extensivo.

---

## 17. Checklist de Contraditorio Interno

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | **CAC + LTV + LTV:CAC 3:1+** calculated cohort-based? | Foundation |
| 2 | **CAC payback <12-18 meses healthy** B2B SaaS? | Efficient growth |
| 3 | **ROAS contextualized com LTV** (not short-term only)? | Full economic view |
| 4 | **Rule of 40 SaaS calculated** (growth + FCF margin ≥40%)? | Valuation lens |
| 5 | **Magic Number quarterly** >0.75 healthy S&M? | Efficiency |
| 6 | **NRR 100%+ healthy** / 110%+ ideal? | Retention |
| 7 | **"So What?" test** applied each metric? | Vanity vigilance |
| 8 | **MTA + MMM dual-model** 2026 norm? | Privacy-first attribution |
| 9 | **Brand health 5 dimensions** tracked monthly/quarterly? | Comprehensive |
| 10 | **Dashboards executive vs tactical** separated? | Decision clarity |

---

## 18. Referencias canonicas

### 18.1 Foundational

- **Sean Ellis** "Hacking Growth" (NSM origin)
- **Brad Feld** Rule of 40 (2015 blog post foundational)
- **Scale Venture Partners** Magic Number (2008 origin)
- **Dave McClure** AARRR Pirate Metrics (cf. `funil-jornada`)
- **Eric Ries** "The Lean Startup" — vanity vs actionable origin

### 18.2 Benchmarks 2026

- **1ClickReport — Marketing KPI Benchmarks 2026** — https://www.1clickreport.com/blog/marketing-kpi-benchmarks-industry-2026
- **Aventis — Rule of 40 SaaS 2026** — https://aventis-advisors.com/rule-of-40-in-saas-2026/
- **Growthspree — LTV:CAC B2B SaaS 2026** — https://www.growthspreeofficial.com/blogs/ltv-cac-ratio-b2b-saas-benchmarks-2026
- **WebFX — Ecommerce Marketing Benchmarks 2026** — https://www.webfx.com/blog/marketing/ecommerce-marketing-benchmarks/
- **SaaS Hero — Performance Marketing KPIs B2B SaaS** — https://www.saashero.net/strategy/performance-marketing-kpis-to-track/

### 18.3 Vanity vs Actionable

- **Userpilot — Vanity vs Actionable SaaS** — https://userpilot.com/blog/vanity-metrics-vs-actionable-metrics-saas/
- **Shopify — Vanity Metrics 101 2026** — https://www.shopify.com/blog/vanity-metrics
- **Improvado — Vanity Metric** — https://improvado.io/blog/what-is-a-vanity-metric

### 18.4 Attribution

- **Improvado — Multi-Touch Attribution 2026** — https://improvado.io/blog/multi-touch-attribution
- **Marketing Mary AI — Attribution Models 2026** — https://www.marketingmary.ai/blog/marketing-attribution-models-guide
- **Digital Applied — Marketing Attribution Statistics 2026 (140 data points)** — https://www.digitalapplied.com/blog/marketing-attribution-statistics-2026-multi-touch
- **Google MMM Library** (Lightweight MMM Bayesian) — open-source 2024
- **Meta Robyn** — open-source MMM

### 18.5 Brand health

- **Sprout Social — Brand Health Tracking 2026** — https://sproutsocial.com/insights/brand-health-tracking/
- **YouScan — Brand Health Tracker** — https://youscan.io/blog/brand-health-tracker/
- **Attest — 13 Brand Health Metrics** — https://www.askattest.com/blog/articles/13-brand-health-metrics-you-need-to-know

### 18.6 SaaS metrics

- **SaaS Metrics Standards Board** — https://www.saasmetricsstandardsboard.org
- **Aventis Advisors — Rule of 40 SaaS 2026** — https://aventis-advisors.com/rule-of-40-in-saas-2026/
- **CFI — Rule of 40 SaaS** — https://corporatefinanceinstitute.com/resources/valuation/rule-of-40/
- **ChartMogul + Baremetrics + ProfitWell** — SaaS metrics tools

### 18.7 Dashboards + tools

- **Looker Studio — Google** — https://lookerstudio.google.com (free)
- **Geckoboard** — https://www.geckoboard.com ($31-149/mês)
- **Whatagraph** — https://whatagraph.com ($199-599/mês)
- **AgencyAnalytics** — https://agencyanalytics.com ($79-279/mês)

### 18.8 Reading

- **"The Lean Startup"** Eric Ries (vanity vs actionable origin)
- **"Lean Analytics"** Alistair Croll + Benjamin Yoskovitz
- **"Hacking Growth"** Sean Ellis + Morgan Brown
- **"Predictably Irrational"** Dan Ariely (decision-making)
- **"How Brands Grow"** Byron Sharp (brand health science)

### 18.9 Brand investment research

- **Binet & Field** (IPA databank) — brand vs performance long-term research
- **"Long and Short of It"** Binet + Field
- **"How Brands Grow"** Byron Sharp + Ehrenberg-Bass Institute

---

## 19. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Métricas + foundation Marketing & Estratégia bloco | `metricas-marketing` + `posicionamento-marca` + `branding` + `funil-jornada` + `big-idea` (anteriores bloco) |
| Métricas + B2B vs B2C audience | `metricas-marketing` + `escrita-por-publico` Sec 4-5 |
| Métricas cross-platform | `metricas-marketing` + `multi-platform-narrative` |
| Métricas community CLG | `metricas-marketing` + `engajamento-comunidade` Sec 7 |
| Métricas SEO | `metricas-marketing` + `seo-fundamentos` Sec 12 |
| Métricas per-platform ads | `metricas-marketing` + `linkedin-ads` + `instagram-ads` + `facebook-ads` + `tiktok-criativo` |
| Métricas brand health | `metricas-marketing` + `branding` Sec 7 |
| Funnel benchmarks B2B SaaS 2026 | `metricas-marketing` + `funil-jornada` Sec 6 |
| Investor reporting Series A-B | `metricas-marketing` + `escrita-por-publico` Sec 6 |
| Attribution + privacy | `metricas-marketing` + `compliance-lgpd` |

---

## 20. Integracao com o ecossistema Frank-MKT

- **Acoplamento com `posicionamento-marca` + `branding` + `funil-jornada` + `big-idea`** (anteriores bloco Marketing & Estratégia) — métricas FECHAM o cycle (positioning → branding → funil → big-idea → MEDIR effectiveness).
- **Acoplamento com `escrita-por-publico` Sec 6** (investor) — métricas align with 2026 efficient growth investor expectations.
- **Acoplamento com `multi-platform-narrative`** — métricas cross-platform attribution.
- **Acoplamento com `engajamento-comunidade` Sec 7** — CLG metrics complementary (activation 20-30% + retention members vs non).
- **Acoplamento com `seo-fundamentos`** + `seo-keywords` + `conteudo-evergreen` — SEO KPIs (organic CAC, traffic, conversions).
- **Acoplamento com skills sociais** (`linkedin-ads`, `instagram-ads`, `facebook-ads`, `tiktok-criativo`) — per-platform metrics + ROAS.
- **Acoplamento com `funil-jornada`** — funnel benchmarks B2B SaaS 2026 + AARRR + NSM + activation rate.
- **Acoplamento com `branding` Sec 7** — brand health tracking 5 dimensions.
- **Acoplamento com `compliance-lgpd`** — privacy-first attribution + first-party data strategy.
- **Acoplamento com `email-marketing` (futura)** — email metrics 6-10x ROAS highest channel.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em metricas (CAC + LTV cohort-based + LTV:CAC 3:1+ + CAC payback <18m + Rule of 40 ≥40% + Magic Number ≥0.75 + NRR ≥100% + "So What?" test + MTA + MMM dual-model + brand health 5 dimensions).
- **Memoria** — `.frank-mkt/metrics/<cliente>/<data>/` (KPI dashboards, attribution model decisions, brand health quarterly results, investor reports, optimization playbooks).
- **Contraditorio interno** — Checklist Sec 17.
- **Decaimento temporal** — volatility `medium` (6 meses) — frameworks (LTV:CAC + R40 + Magic Number + vanity vs actionable) decadas estaveis; benchmarks 2026 + privacy regulations + attribution models atualizam moderadamente.
- **Regra de ouro para `frank-mkt`** — nenhum KPI definition, dashboard, attribution model, OR investor report sai do plugin sem passar por esta skill.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a brand, audiencia, mercado, contexto cultural local (BR + global), e validadas com finance team alignment + cohort analysis + benchmark comparison industry antes de aplicar em metricas reais. Esta e uma skill de volatility `medium` (6 meses) — frameworks foundational decadas estaveis; benchmarks 2026 + privacy regulations + attribution shifts atualizam moderadamente.

---

*Plugin `frank-mkt` — skill `metricas-marketing` (v0.1.0)*
*Ultima atualizacao: 2026-05-08*
*Pesquisa de campo: 6 web searches em 2026-05-08 (marketing KPIs 2026 CAC LTV ROAS benchmarks B2B SaaS B2C ecommerce, Magic Number Rule of 40 SaaS metrics 2026 unit economics formulas, vanity metrics actionable metrics 2026 marketing analytics framework, marketing attribution 2026 multi-touch model first-touch last-touch data-driven, marketing dashboard 2026 Looker Studio Geckoboard tools metrics visualization, brand health metrics 2026 NPS sentiment recall awareness measurement)*

Sources used in field research (web search 2026-05-08):
- [1ClickReport — Marketing KPI Benchmarks 2026](https://www.1clickreport.com/blog/marketing-kpi-benchmarks-industry-2026)
- [Aventis Advisors — Rule of 40 SaaS 2026](https://aventis-advisors.com/rule-of-40-in-saas-2026/)
- [Growthspree — LTV:CAC B2B SaaS Benchmarks 2026](https://www.growthspreeofficial.com/blogs/ltv-cac-ratio-b2b-saas-benchmarks-2026)
- [Userpilot — Vanity vs Actionable SaaS](https://userpilot.com/blog/vanity-metrics-vs-actionable-metrics-saas/)
- [Improvado — Multi-Touch Attribution 2026](https://improvado.io/blog/multi-touch-attribution)
- [Sprout Social — Brand Health Tracking 2026](https://sproutsocial.com/insights/brand-health-tracking/)
- [Looker Studio vs Geckoboard 2026](https://www.selecthub.com/data-visualization-tools/looker-studio-vs-geckoboard/)
- [SelectHub — Looker Studio vs Geckoboard](https://www.selecthub.com/data-visualization-tools/looker-studio-vs-geckoboard/)
- [Wikipedia — Rule of 40](https://en.wikipedia.org/wiki/Rule_of_40)
- [Marketing Mary AI — Attribution Models 2026](https://www.marketingmary.ai/blog/marketing-attribution-models-guide)
