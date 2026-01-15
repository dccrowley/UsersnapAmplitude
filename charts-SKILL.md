# Chart Implementation Patterns

## Donut Charts

Best for part-to-whole relationships with 5 or fewer segments.

### Design Rules

- Maximum **5 segments** (7 absolute max, group smaller into "Other")
- Inner radius approximately **40%** of outer radius
- Use centre space for total value or key metric
- Sort slices descending, starting at 12 o'clock
- Direct label on slices, avoid legends when possible
- Add subtle segment gaps (1-2px) for visual separation

### React Implementation (Recharts)

```jsx
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

const COLOURS = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'];

const DonutChart = ({ data, centreValue, centreLabel }) => (
  <div className="donut-container">
    <ResponsiveContainer width="100%" height={240}>
      <PieChart>
        <Pie
          data={data}
          cx="50%"
          cy="50%"
          innerRadius={60}
          outerRadius={100}
          paddingAngle={2}
          dataKey="value"
          startAngle={90}
          endAngle={-270}
          animationDuration={800}
          animationEasing="ease-out"
        >
          {data.map((entry, index) => (
            <Cell 
              key={entry.name} 
              fill={COLOURS[index % COLOURS.length]}
              stroke="none"
            />
          ))}
        </Pie>
      </PieChart>
    </ResponsiveContainer>
    <div className="donut-centre">
      <span className="donut-value">{centreValue}</span>
      <span className="donut-label">{centreLabel}</span>
    </div>
  </div>
);
```

### CSS for Donut Centre Label

```css
.donut-container {
  position: relative;
}

.donut-centre {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.donut-value {
  display: block;
  font-size: 32px;
  font-weight: 700;
  line-height: 1;
  color: var(--neutral-900);
}

.donut-label {
  display: block;
  font-size: 12px;
  font-weight: 500;
  color: var(--neutral-500);
  margin-top: 4px;
}
```

---

## Bar Charts

Best for comparing discrete categories.

### Design Rules

- **Always start Y-axis at zero** (non-negotiable for bars)
- Use **horizontal bars** for long category labels
- Apply **rounded corners** (4-8px radius) for modern aesthetic
- Sort bars by value (ascending or descending) unless natural order exists
- Direct label values at end of bars when space permits
- Consistent bar width, use spacing to separate groups

### React Implementation (Recharts)

```jsx
import { BarChart, Bar, XAxis, YAxis, ResponsiveContainer, Cell, LabelList } from 'recharts';

const HorizontalBarChart = ({ data, colour = '#3B82F6' }) => (
  <ResponsiveContainer width="100%" height={data.length * 48 + 40}>
    <BarChart
      data={data}
      layout="vertical"
      margin={{ top: 8, right: 80, left: 120, bottom: 8 }}
    >
      <XAxis type="number" hide />
      <YAxis 
        type="category" 
        dataKey="name" 
        axisLine={false}
        tickLine={false}
        tick={{ fontSize: 14, fill: '#525252' }}
        width={110}
      />
      <Bar 
        dataKey="value" 
        radius={[0, 6, 6, 0]}
        animationDuration={600}
        animationEasing="ease-out"
      >
        {data.map((entry, index) => (
          <Cell key={entry.name} fill={colour} />
        ))}
        <LabelList 
          dataKey="value" 
          position="right" 
          formatter={(v) => v.toLocaleString()}
          style={{ fontSize: 14, fontWeight: 600, fill: '#171717' }}
        />
      </Bar>
    </BarChart>
  </ResponsiveContainer>
);
```

### Grouped Bar Variant

```jsx
const GroupedBarChart = ({ data, keys, colours }) => (
  <ResponsiveContainer width="100%" height={300}>
    <BarChart data={data} margin={{ top: 16, right: 16, left: 0, bottom: 24 }}>
      <XAxis 
        dataKey="category" 
        axisLine={false}
        tickLine={false}
        tick={{ fontSize: 12, fill: '#737373' }}
      />
      <YAxis 
        axisLine={false}
        tickLine={false}
        tick={{ fontSize: 12, fill: '#737373' }}
        tickFormatter={(v) => v.toLocaleString()}
      />
      {keys.map((key, i) => (
        <Bar 
          key={key}
          dataKey={key} 
          fill={colours[i]}
          radius={[4, 4, 0, 0]}
          maxBarSize={40}
        />
      ))}
    </BarChart>
  </ResponsiveContainer>
);
```

---

## Area Charts

Best for showing trends over time, especially cumulative data.

### Design Rules

- Use **gradient fills** with transparency for depth
- Stack areas when showing composition over time
- Smooth curves (monotone interpolation) for organic feel
- Grid lines should be subtle (10-15% opacity)
- Highlight the most recent data point

### React Implementation (Recharts)

```jsx
import { AreaChart, Area, XAxis, YAxis, ResponsiveContainer, Tooltip } from 'recharts';

const GradientAreaChart = ({ data, dataKey, colour = '#3B82F6' }) => (
  <ResponsiveContainer width="100%" height={240}>
    <AreaChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 8 }}>
      <defs>
        <linearGradient id={`gradient-${dataKey}`} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor={colour} stopOpacity={0.3} />
          <stop offset="100%" stopColor={colour} stopOpacity={0.05} />
        </linearGradient>
      </defs>
      <XAxis 
        dataKey="date"
        axisLine={false}
        tickLine={false}
        tick={{ fontSize: 11, fill: '#A3A3A3' }}
        tickFormatter={(d) => new Date(d).toLocaleDateString('en-GB', { month: 'short' })}
      />
      <YAxis 
        axisLine={false}
        tickLine={false}
        tick={{ fontSize: 11, fill: '#A3A3A3' }}
        tickFormatter={(v) => v >= 1000 ? `${v/1000}k` : v}
        width={48}
      />
      <Tooltip 
        contentStyle={{
          background: '#171717',
          border: 'none',
          borderRadius: 8,
          padding: '8px 12px',
          fontSize: 13,
          color: '#FAFAFA'
        }}
      />
      <Area
        type="monotone"
        dataKey={dataKey}
        stroke={colour}
        strokeWidth={2}
        fill={`url(#gradient-${dataKey})`}
        animationDuration={800}
      />
    </AreaChart>
  </ResponsiveContainer>
);
```

---

## Sankey Diagrams

Best for showing flows, conversions, and resource allocation.

### Design Rules

- Place related nodes close together (Gestalt proximity)
- Use consistent colours for related flows
- Same category = same colour throughout
- Give important elements space to breathe
- Keep labels horizontal when possible
- Flow width proportional to value

### React Implementation (D3-based)

Sankey requires D3. Use with react wrapper or direct DOM manipulation:

```jsx
import { useRef, useEffect } from 'react';
import * as d3 from 'd3';
import { sankey, sankeyLinkHorizontal } from 'd3-sankey';

const SankeyDiagram = ({ data, width = 600, height = 400 }) => {
  const svgRef = useRef();

  useEffect(() => {
    const svg = d3.select(svgRef.current);
    svg.selectAll('*').remove();

    const sankeyGenerator = sankey()
      .nodeWidth(20)
      .nodePadding(16)
      .extent([[16, 16], [width - 16, height - 16]]);

    const { nodes, links } = sankeyGenerator(data);

    // Links
    svg.append('g')
      .selectAll('path')
      .data(links)
      .join('path')
      .attr('d', sankeyLinkHorizontal())
      .attr('fill', 'none')
      .attr('stroke', d => d.source.colour || '#94A3B8')
      .attr('stroke-opacity', 0.4)
      .attr('stroke-width', d => Math.max(1, d.width))
      .on('mouseenter', function() {
        d3.select(this).attr('stroke-opacity', 0.7);
      })
      .on('mouseleave', function() {
        d3.select(this).attr('stroke-opacity', 0.4);
      });

    // Nodes
    svg.append('g')
      .selectAll('rect')
      .data(nodes)
      .join('rect')
      .attr('x', d => d.x0)
      .attr('y', d => d.y0)
      .attr('height', d => d.y1 - d.y0)
      .attr('width', d => d.x1 - d.x0)
      .attr('fill', d => d.colour || '#3B82F6')
      .attr('rx', 4);

    // Labels
    svg.append('g')
      .selectAll('text')
      .data(nodes)
      .join('text')
      .attr('x', d => d.x0 < width / 2 ? d.x1 + 8 : d.x0 - 8)
      .attr('y', d => (d.y0 + d.y1) / 2)
      .attr('dy', '0.35em')
      .attr('text-anchor', d => d.x0 < width / 2 ? 'start' : 'end')
      .attr('font-size', 12)
      .attr('fill', '#525252')
      .text(d => d.name);

  }, [data, width, height]);

  return <svg ref={svgRef} width={width} height={height} />;
};
```

---

## Line Charts

Best for showing trends and comparing multiple series.

### Design Rules

- Use distinct colours with sufficient contrast between lines
- Add dots at data points for precision reading
- Highlight the most recent value with larger marker
- Use dashed lines for projections/forecasts
- Maximum 5-6 lines before chart becomes cluttered

### React Implementation (Recharts)

```jsx
import { LineChart, Line, XAxis, YAxis, ResponsiveContainer, Tooltip, Legend } from 'recharts';

const MultiLineChart = ({ data, lines }) => (
  <ResponsiveContainer width="100%" height={280}>
    <LineChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 8 }}>
      <XAxis 
        dataKey="date"
        axisLine={false}
        tickLine={false}
        tick={{ fontSize: 11, fill: '#A3A3A3' }}
      />
      <YAxis 
        axisLine={false}
        tickLine={false}
        tick={{ fontSize: 11, fill: '#A3A3A3' }}
        width={48}
      />
      <Tooltip 
        contentStyle={{
          background: '#171717',
          border: 'none',
          borderRadius: 8,
          fontSize: 13,
          color: '#FAFAFA'
        }}
      />
      {lines.map(({ key, colour, dashed }) => (
        <Line
          key={key}
          type="monotone"
          dataKey={key}
          stroke={colour}
          strokeWidth={2}
          strokeDasharray={dashed ? '6 4' : undefined}
          dot={{ r: 3, fill: colour }}
          activeDot={{ r: 5, fill: colour }}
          animationDuration={800}
        />
      ))}
    </LineChart>
  </ResponsiveContainer>
);
```

---

## KPI Cards

Hero metrics displayed prominently.

### Design Rules

- One primary value per card (36-48px bold)
- Secondary context below (trend, comparison, label)
- Use semantic colours for trend indicators
- Subtle background or border to define card boundary
- Icon optional, should reinforce meaning not decorate

### React Implementation

```jsx
const KPICard = ({ 
  title, 
  value, 
  trend, 
  trendValue, 
  subtitle,
  icon: Icon 
}) => {
  const trendColour = trend === 'up' 
    ? 'var(--semantic-positive)' 
    : trend === 'down' 
    ? 'var(--semantic-negative)' 
    : 'var(--semantic-neutral)';

  return (
    <div className="kpi-card">
      <div className="kpi-header">
        <span className="kpi-title">{title}</span>
        {Icon && <Icon className="kpi-icon" />}
      </div>
      <div className="kpi-value">{value}</div>
      <div className="kpi-footer">
        {trendValue && (
          <span className="kpi-trend" style={{ color: trendColour }}>
            {trend === 'up' ? '↑' : trend === 'down' ? '↓' : '→'} {trendValue}
          </span>
        )}
        {subtitle && <span className="kpi-subtitle">{subtitle}</span>}
      </div>
    </div>
  );
};
```

### CSS for KPI Card

```css
.kpi-card {
  background: var(--neutral-50);
  border: 1px solid var(--neutral-200);
  border-radius: 12px;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.kpi-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.kpi-title {
  font-size: 14px;
  font-weight: 500;
  color: var(--neutral-600);
}

.kpi-icon {
  width: 20px;
  height: 20px;
  color: var(--neutral-400);
}

.kpi-value {
  font-size: 36px;
  font-weight: 700;
  line-height: 1;
  color: var(--neutral-900);
  font-variant-numeric: tabular-nums;
}

.kpi-footer {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
}

.kpi-trend {
  font-weight: 600;
}

.kpi-subtitle {
  color: var(--neutral-500);
}
```

---

## Sparklines

Compact trend indicators for tables and dense layouts.

### Design Rules

- No axes, labels, or grid
- Single colour, simple line
- Optional: highlight min/max/current with dots
- Fixed height (24-40px typically)

### React Implementation

```jsx
import { LineChart, Line, ResponsiveContainer, ReferenceDot } from 'recharts';

const Sparkline = ({ data, dataKey = 'value', colour = '#3B82F6', height = 32 }) => {
  const lastIndex = data.length - 1;
  const lastValue = data[lastIndex]?.[dataKey];
  
  return (
    <ResponsiveContainer width="100%" height={height}>
      <LineChart data={data} margin={{ top: 4, right: 8, left: 0, bottom: 4 }}>
        <Line
          type="monotone"
          dataKey={dataKey}
          stroke={colour}
          strokeWidth={1.5}
          dot={false}
        />
        <ReferenceDot
          x={data[lastIndex]?.date}
          y={lastValue}
          r={3}
          fill={colour}
          stroke="none"
        />
      </LineChart>
    </ResponsiveContainer>
  );
};
```

---

## Data Tables

For detailed data exploration alongside charts.

### Design Rules

- Align text left, numbers right
- Use tabular-nums for numeric columns
- Subtle alternating row backgrounds or horizontal dividers
- Highlight hover row
- Sort indicators clear but not dominant
- Pagination or virtual scroll for large datasets

### CSS Foundation

```css
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.data-table th {
  text-align: left;
  font-weight: 600;
  color: var(--neutral-700);
  padding: 12px 16px;
  border-bottom: 2px solid var(--neutral-200);
  white-space: nowrap;
}

.data-table th[data-type="number"] {
  text-align: right;
}

.data-table td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--neutral-100);
  color: var(--neutral-800);
}

.data-table td[data-type="number"] {
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum';
}

.data-table tr:hover {
  background: var(--neutral-50);
}

.data-table tr:last-child td {
  border-bottom: none;
}
```

---

## Animation Patterns

### Staggered Entrance

```css
.widget {
  opacity: 0;
  transform: translateY(12px);
  animation: widget-enter 0.5s ease-out forwards;
}

.widget:nth-child(1) { animation-delay: 0ms; }
.widget:nth-child(2) { animation-delay: 80ms; }
.widget:nth-child(3) { animation-delay: 160ms; }
.widget:nth-child(4) { animation-delay: 240ms; }

@keyframes widget-enter {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### Number Count-Up

```jsx
import { useEffect, useState } from 'react';

const AnimatedNumber = ({ value, duration = 800 }) => {
  const [display, setDisplay] = useState(0);

  useEffect(() => {
    const start = performance.now();
    const startValue = display;
    
    const animate = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      setDisplay(Math.round(startValue + (value - startValue) * eased));
      
      if (progress < 1) requestAnimationFrame(animate);
    };
    
    requestAnimationFrame(animate);
  }, [value]);

  return <span>{display.toLocaleString()}</span>;
};
```

### Chart Draw-On Effect (CSS)

```css
.chart-line {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  animation: draw-line 1.2s ease-out forwards;
}

@keyframes draw-line {
  to {
    stroke-dashoffset: 0;
  }
}
```

### Reduced Motion Support

Always include:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```
