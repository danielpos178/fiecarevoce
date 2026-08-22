<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
                xmlns:html="http://www.w3.org/TR/REC-html40"
                xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="ro">
      <head>
        <title>Harta Site-ului XML (Sitemap) | Fiecare Voce</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style type="text/css">
          * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
          }
          body {
            font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #fcfbf9;
            color: #1a1c19;
            padding: 2rem 1rem;
            line-height: 1.5;
          }
          .container {
            max-width: 1200px;
            margin: 0 auto;
          }
          .header {
            background-color: #1b4332;
            color: #ffffff;
            border: 3px solid #1a1c19;
            box-shadow: 6px 6px 0px 0px #1a1c19;
            padding: 2rem;
            margin-bottom: 2rem;
          }
          .badge {
            display: inline-block;
            background-color: #ffd166;
            color: #1a1c19;
            font-weight: 900;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.25rem 0.75rem;
            border: 2px solid #1a1c19;
            box-shadow: 2px 2px 0px 0px #1a1c19;
            margin-bottom: 1rem;
          }
          h1 {
            font-size: 2.25rem;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: -0.02em;
            margin-bottom: 0.5rem;
          }
          p.subtitle {
            color: #d1e7dd;
            font-size: 1rem;
            max-width: 800px;
          }
          .stats {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
          }
          .stat-box {
            background-color: #ffffff;
            color: #1a1c19;
            border: 2px solid #1a1c19;
            box-shadow: 3px 3px 0px 0px #1a1c19;
            padding: 0.75rem 1.25rem;
            font-weight: 700;
            font-size: 0.875rem;
            text-transform: uppercase;
          }
          .stat-box span {
            color: #1b4332;
            font-size: 1.125rem;
            font-weight: 900;
            margin-left: 0.5rem;
          }
          .table-container {
            background-color: #ffffff;
            border: 3px solid #1a1c19;
            box-shadow: 6px 6px 0px 0px #1a1c19;
            overflow-x: auto;
          }
          table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.875rem;
          }
          th {
            background-color: #1a1c19;
            color: #ffffff;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 1rem;
            border-bottom: 3px solid #1a1c19;
          }
          td {
            padding: 0.875rem 1rem;
            border-bottom: 1px solid #e5e7eb;
            vertical-align: middle;
          }
          tr:nth-child(even) {
            background-color: #f9fafb;
          }
          tr:hover {
            background-color: #e8f5e9;
          }
          a {
            color: #1b4332;
            text-decoration: none;
            font-weight: 700;
            word-break: break-all;
          }
          a:hover {
            text-decoration: underline;
            color: #2d6a4f;
          }
          .priority-tag {
            display: inline-block;
            padding: 0.2rem 0.5rem;
            font-weight: 800;
            font-size: 0.75rem;
            border: 1px solid #1a1c19;
            background-color: #e2e8f0;
          }
          .priority-high {
            background-color: #d1e7dd;
            color: #0f5132;
            border-color: #0f5132;
          }
          .priority-top {
            background-color: #ffd166;
            color: #1a1c19;
            border-color: #1a1c19;
          }
          .freq-tag {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            color: #4b5563;
          }
          .date-tag {
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 0.8rem;
            color: #374151;
          }
          .footer {
            margin-top: 2rem;
            text-align: center;
            font-size: 0.875rem;
            color: #6b7280;
            font-weight: 600;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <div class="badge">XML</div>
            <h1>Sitemap XML</h1>
            <div class="stats">
              <div class="stat-box">
                Total Adrese Indexabile: <span><xsl:value-of select="count(sitemap:urlset/sitemap:url)"/></span>
              </div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th style="width: 5%;">#</th>
                  <th style="width: 50%;">URL (Adresă Pagină)</th>
                  <th style="width: 10%;">Prioritate</th>
                  <th style="width: 15%;">Frecvență</th>
                  <th style="width: 20%;">Ultima Modificare</th>
                </tr>
              </thead>
              <tbody>
                <xsl:for-each select="sitemap:urlset/sitemap:url">
                  <tr>
                    <td><strong><xsl:value-of select="position()"/></strong></td>
                    <td>
                      <a href="{sitemap:loc}" target="_blank">
                        <xsl:value-of select="sitemap:loc"/>
                      </a>
                    </td>
                    <td>
                      <xsl:variable name="prio" select="sitemap:priority"/>
                      <span class="priority-tag">
                        <xsl:choose>
                          <xsl:when test="$prio = '1.0'">
                            <xsl:attribute name="class">priority-tag priority-top</xsl:attribute>
                          </xsl:when>
                          <xsl:when test="$prio &gt;= 0.8">
                            <xsl:attribute name="class">priority-tag priority-high</xsl:attribute>
                          </xsl:when>
                        </xsl:choose>
                        <xsl:value-of select="sitemap:priority"/>
                      </span>
                    </td>
                    <td>
                      <span class="freq-tag">
                        <xsl:value-of select="sitemap:changefreq"/>
                      </span>
                    </td>
                    <td>
                      <span class="date-tag">
                        <xsl:value-of select="substring(sitemap:lastmod, 0, 11)"/>&#160;<xsl:value-of select="substring(sitemap:lastmod, 12, 5)"/>
                      </span>
                    </td>
                  </tr>
                </xsl:for-each>
              </tbody>
            </table>
          </div>

          <div class="footer">
            Generat automat de platforma independentă <strong>Fiecare Voce</strong> • Toate drepturile rezervate.
          </div>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
